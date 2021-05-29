import requests
from json import loads, dumps
import os
import settings
from help_methods import catch
from json import loads

# old/new currency - str


def if_file_exist():
    return os.path.exists("currency.json")


class CurrencyConverter:
    if(not if_file_exist()):
        file = open("currency.json", "w")
        file.write("{}")
        file.close()

    with open("currency.json", "r") as tranzaction_rules:
        values_convert = loads(tranzaction_rules.read())

    @staticmethod
    def get_request(old_currency, new_currency):
        return loads(requests.get(f"https://free.currencyconverterapi.com/api/v6/convert?q={old_currency}_{new_currency}&compact=ultra&apiKey={settings.TOKEN}").text)

    @staticmethod
    def convert(values, old_currency, new_currency):
        if(CurrencyConverter.values_convert.get(f"{old_currency}_{new_currency}") is not None):
            return values * CurrencyConverter.values_convert[f"{old_currency}_{new_currency}"]
        else:
            return CurrencyConverter.addCurrency(values, old_currency, new_currency)

    @ staticmethod
    @ catch
    def add_currency(values: float, old_currency: str, new_currency: str) -> float:
        "вычислить валюту в новой валюте"
        r=CurrencyConverter.get_request(old_currency, new_currency)
        CurrencyConverter.values_convert[f"{old_currency}_{new_currency}"]=r.json()[
            f"{old_currency}_{new_currency}"]

        with open("currency.json", "w") as tranzaction_write:
            tranzaction_write.write(dumps(CurrencyConverter.values_convert))
        return values * CurrencyConverter.values_convert[f"{old_currency}_{new_currency}"]

if __name__ == "__main__":
    print(if_file_exist())
#    print(settings.TOKEN)
    print(CurrencyConverter.get_request("RUB", "EUR"))
