from flask import Flask, jsonify, request
import os
from CurrencyConverter import if_file_exist, CurrencyConverter
from controllers import MoneyController
from json import loads
from help_methods import get_money_name, catch
app = Flask(__name__)


@app.route("/", methods=['GET'])
def view():
    if (if_file_exist()):
        with open("currency.json", mode="r") as head_file_converter:
            info = {item["name_k"]: item["koef"]
                    for item in MoneyController.get_all()}
            return jsonify(info)
    else:
        jsonify(dict(status="file not exist"))


@app.route("/view_currency/value=<value>&old_currency=<old_currency>&new_currency=<new_currency>",
           methods=['GET'])
@catch
def view_currency(value, old_currency, new_currency):
    money_on_bd = MoneyController.get_by_name(old_currency, new_currency)

    if(money_on_bd is None):
        MoneyController.create_money_k(
            old_currency, new_currency, r)

        money_on_bd = MoneyController.get_by_name(old_currency, new_currency)
        info = {get_money_name(old_currency, new_currency, "->"): float(value)*money_on_bd.koef}
    else:
        info = {get_money_name(old_currency, new_currency, '->'): float(value)*money_on_bd.koef}
    return info


@app.route("/old_currency=<old_currency>&new_currency=<new_currency>", methods=["PUT"])
@catch
def update_currency(old_currency, new_currency):
    r = CurrencyConverter.get_request(old_currency, new_currency)
    update_info = MoneyController(
        get_money_name(old_currency, new_currency))
    update_info.update_money_k(r[get_money_name(old_currency, new_currency)])

    json_v = {"status": "OK", get_money_name(
        old_currency, new_currency, "->"): r[get_money_name(old_currency, new_currency)]}
    return jsonify(json_v)


@app.route("/old_currency=<old_currency>&new_currency=<new_currency>", methods=["DELETE"])
@catch
def remove_currency(old_currency, new_currency):
    MoneyController.remove_currency(get_money_name(old_currency, new_currency))
    return jsonify(dict(status="OK"))

if __name__ == "__main__":
    app.run(debug=True, port=5000)
