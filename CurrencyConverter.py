import requests
from json import loads, dumps
import os
import settings
from help_methods import catch, get_money_name
from json import loads
from controllers import MoneyController
# old/new currency - str


def if_file_exist() -> bool:
    return os.path.exists("currency.json")


class CurrencyConverter:
    @staticmethod
    def get_request(old_currency:str, new_currency:str) -> loads:
        return loads(requests.get(f"https://free.currencyconverterapi.com/api/v6/convert?q={old_currency}_{new_currency}&compact=ultra&apiKey={settings.TOKEN}").text)

    @staticmethod
    def convert(values:float, old_currency:str, new_currency:str)->float:
        name_v = MoneyController.get_by_name(old_currency, new_currency)
        return values * name_v.koef
    
    @ staticmethod
    def add_currency(values: float, old_currency: str, new_currency: str) -> float:
        "вычислить валюту в новой валюте"
        r=CurrencyConverter.get_request(old_currency, new_currency)
        MoneyController.create_money_k(old_currency, new_currency, r[get_money_name(old_currency, new_currency)])
        return values * r[get_money_name(old_currency, new_currency)]

if __name__ == "__main__":
    print(if_file_exist())
#    print(settings.TOKEN)
    print(CurrencyConverter.add_currency(100.0, "USD", "EUR"))