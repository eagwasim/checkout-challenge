import abc


class PricingRule:
    def __init__(self, discount):
        self.discount = discount

    @abc.abstractmethod
    def apply(self, item):
        pass


class TwoForOne(PricingRule):

    def apply(self, item):
        total_eligible_item_count_less_modulus = item.quantity - (item.quantity % 2)

        print(total_eligible_item_count_less_modulus)

        actual_amount_for_eligible_count = total_eligible_item_count_less_modulus * item.unit_price

        actual_amount_for_ineligible_count = (item.quantity % 2) * item.unit_price

        discounted_amount_for_eligible_count = actual_amount_for_eligible_count - (
                actual_amount_for_eligible_count * self.discount)

        item.total_price = discounted_amount_for_eligible_count + actual_amount_for_ineligible_count

        return item


class BulkPurchase(PricingRule):
    def apply(self, item):
        if item.quantity >= 3:
            actual_amount_for_eligible_count = (item.quantity * item.unit_price)

            discounted_amount_for_eligible_count = actual_amount_for_eligible_count - (
                    actual_amount_for_eligible_count * self.discount)

            item.total_price = discounted_amount_for_eligible_count

        return item
