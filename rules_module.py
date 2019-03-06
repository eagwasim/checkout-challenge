import abc

"""
This module contains all the rules that are applicable in the application
"""


class PricingRule:
    """
    An abstract class that all rules must inherit from so they are forced to provide uniform functionality
    """

    def __init__(self, discount):
        self.discount = discount

    @abc.abstractmethod
    def apply(self, item):
        pass


class TwoForOne(PricingRule):
    """
    The Two for one rule basically gives a discount for every two item purchased
    """

    def apply(self, item):
        total_eligible_item_count_less_modulus = item.quantity - (item.quantity % 2)

        actual_amount_for_eligible_count = total_eligible_item_count_less_modulus * item.unit_price

        actual_amount_for_ineligible_count = (item.quantity % 2) * item.unit_price

        discounted_amount_for_eligible_count = actual_amount_for_eligible_count - (
                actual_amount_for_eligible_count * self.discount)

        item.total_price = discounted_amount_for_eligible_count + actual_amount_for_ineligible_count

        return item


class BulkPurchase(PricingRule):
    """
    The Bulk buy rule rule gives a general discount when three or more items are purchased
    """

    def apply(self, item):
        if item.quantity >= 3:
            actual_amount_for_eligible_count = (item.quantity * item.unit_price)

            discounted_amount_for_eligible_count = actual_amount_for_eligible_count - (
                    actual_amount_for_eligible_count * self.discount)

            item.total_price = discounted_amount_for_eligible_count

        return item
