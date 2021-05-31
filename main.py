from flask import Flask, jsonify, request
import os
from CurrencyConverter import if_file_exist, CurrencyConverter
from controllers import MoneyController
from json import loads
from help_methods import get_money_name, catch

app = Flask(__name__)


@app.route("/", methods=['GET'])
@catch
def view():
    info = {item["name_k"]: item["koef"] for item in MoneyController.get_all()}
    return jsonify(info)


@app.route(
    "/view_currency/value=<value>&old_currency=<old_currency>&new_currency=<new_currency>",
    methods=['GET'])
@catch
def view_currency(value, old_currency, new_currency):
    money_on_bd = MoneyController.get_by_name(old_currency, new_currency)

    if (money_on_bd is None):
        money_on_bd_value = CurrencyConverter.add_currency(
            float(value), old_currency, new_currency)
        info = {
            get_money_name(old_currency, new_currency, "->"): money_on_bd_value
        }
    else:
        info = {
            get_money_name(old_currency, new_currency, '->'):
            CurrencyConverter.convert(float(value), old_currency, new_currency)
        }
    return info


@app.route("/old_currency=<old_currency>&new_currency=<new_currency>",
           methods=["PUT"])
@catch
def update_currency(old_currency, new_currency):
    r = CurrencyConverter.get_request(old_currency, new_currency)

    update_info = MoneyController(get_money_name(old_currency, new_currency))

    update_info.update_money_k(r[get_money_name(old_currency, new_currency)])

    json_v = {
        "status":
        "OK",
        get_money_name(old_currency, new_currency, "->"):
        r[get_money_name(old_currency, new_currency)]
    }

    return jsonify(json_v)


@app.route(
    "/ratio=<ratio>&old_currency=<old_currency>&new_currency=<new_currency>",
    methods=["PUT"])
@catch
def custom_update_currency(ratio, old_currency, new_currency):
    update_info = MoneyController(get_money_name(old_currency, new_currency))

    update_info.update_money_k(float(ratio))

    json_v = {
        "status": "OK",
        get_money_name(old_currency, new_currency, "->"): float(ratio)
    }

    return jsonify(json_v)


@app.route("/old_currency=<old_currency>&new_currency=<new_currency>",
           methods=["DELETE"])
@catch
def remove_currency(old_currency, new_currency):
    remove_currency = MoneyController.get_by_name(old_currency, new_currency)
    MoneyController.remove_currency(old_currency, new_currency)
    return jsonify(dict(status="OK", delete=remove_currency.name_k))


@app.route(
    "/ratio=<ratio>&old_currency=<old_currency>&new_currency=<new_currency>",
    methods=["POST"])
@catch
def create_new_currency(ratio, old_currency, new_currency):
    q = MoneyController.create_money_k(old_currency, new_currency,
                                       float(ratio))
    return jsonify(
        dict(status="OK",
             create_new_currency=f"{old_currency} -> {new_currency}"))


if __name__ == "__main__":
    app.run(debug=True, port=5000)
