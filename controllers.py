from models import Money
from playhouse.shortcuts import model_to_dict, dict_to_model
from help_methods import get_money_name

class MoneyController():
    def __init__(self, name_m:str):
        self.name_m = Money.get_by_id(name_m)

    @staticmethod
    def create_money_k(old_money:str, new_money:str, koef:float)->Money:
        try:
            money = Money.get_or_create(
                name_k=get_money_name(old_money, new_money), koef=koef)
            return money
        except Exception as e:
            print(f"Fail: {e}")
            return 0

    @staticmethod
    def get_all() -> list:
        money = Money.select()
        return list(money.dicts())

    def update_money_k(self, koef: float) -> None:
        self.name_m.koef = koef
        self.name_m.save()

    @staticmethod
    def get_by_name(old_money: str, new_money: str) -> Money:
        money = Money.get_or_none(name_k=get_money_name(old_money, new_money))
        return money

    @staticmethod
    def remove_currency(old_money: str, new_money: str) -> None:
        money = Money.get_or_none(name_k=get_money_name(old_money, new_money))
        money.delete_instance()


if __name__ == '__main__':
    from pprint import pprint
    from json import loads
  #  money_c = MoneyController("USD_RUB")
  #  money_c.update_money_k(75.0)
    print(MoneyController.get_by_name("RUB", "USD"))
