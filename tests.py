from unittest import TestCase
import controllers
import help_methods
import CurrencyConverter


class ControllersTest(TestCase):
    def test_get_all(self):
        q = controllers.MoneyController.get_all()
        self.assertEqual(q is not None, True)

    def test_get_by_name(self):
        q = controllers.MoneyController.get_by_name("USD", "RUB")
        self.assertEqual(q.koef != None, True)


class HelpMethodsTest(TestCase):
    def test_get_money_name(self):
        q = help_methods.get_money_name("RUB", "USD", symbol="->")
        self.assertEqual(q == "RUB->USD", True)


class CurrencyConverterTest(TestCase):
    def test_get_request(self):
        q = CurrencyConverter.CurrencyConverter.get_request("USD", "RUB")
        self.assertEqual(q!=None and q!={}, True)
    def test_convert(self):
        q = CurrencyConverter.CurrencyConverter.convert(100, "USD", "RUB")
        self.assertEqual(q!=None and q!={}, True)