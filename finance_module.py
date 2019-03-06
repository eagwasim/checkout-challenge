class Checkout:
    def __init__(self, cart, pricing_service):
        self.cart = cart
        self.pricing_service = pricing_service

    def get_total(self):
        total_sum = 0

        for item in self.cart.values():
            item = self.pricing_service.apply_rule(item=item)
            total_sum = total_sum + item.total_price

        return total_sum
