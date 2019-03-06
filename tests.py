import unittest

from finance_module import CheckOut
from input_module import parse_input
from model_module import Item
from pricing_module import PricingService
from rules_module import TwoForOne, BulkPurchase


class Test(unittest.TestCase):
    def test_correct_parsing(self):
        """Test case to ensure the correct input is gotten at all times"""
        self.assertListEqual(['BOY', 'GIRL', 'MAN', 'WOMAN'], parse_input('BOY, GIRL, MAN69WOMAN'))

    def test_two_for_one(self):
        """Test case to ensure the the two for one rule is correctly applied"""
        pricing_rule = TwoForOne(discount=1.0 / 2.0)
        item = Item(name="Test", code="TEST", unit_price=100)

        item.increment()
        item.increment()
        item.increment()
        item.increment()

        self.assertEqual(200.00, pricing_rule.apply(item).total_price)

    def test_bulk_purchase(self):
        """Test case to ensure the the bulk purchase rule is correctly applied"""
        pricing_rule = BulkPurchase(discount=1.0 / 100.00)
        item = Item(name="Test", code="TEST", unit_price=100)

        item.increment()
        item.increment()
        item.increment()
        item.increment()

        self.assertEqual(99.0 * 4, pricing_rule.apply(item).total_price)

    def test_check_out(self):
        """Test case to ensure the checkout service works correctly"""
        pricing_service = PricingService()
        pricing_service.register("TEST1", TwoForOne(discount=1.0 / 2.0))
        pricing_service.register("TEST2", BulkPurchase(discount=1.0 / 20.0))

        cart = {}

        item = Item(name="Test", code="TEST1", unit_price=100.00)

        item.increment()
        item.increment()
        item.increment()
        item.increment()

        cart['TEST1'] = item

        item = Item(name="Test", code="TEST2", unit_price=20.00)

        item.increment()
        item.increment()
        item.increment()
        item.increment()

        cart['TEST2'] = item

        checkout = CheckOut(cart, pricing_service)

        self.assertEqual(276, checkout.get_total())


if __name__ == '__main__':
    unittest.main()
