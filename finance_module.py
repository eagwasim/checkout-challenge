class CheckOut:
    """
    The checkout service handles the calculation of all the individual item amounts after the price rules have been applied
    """

    def __init__(self, cart, pricing_service):
        """
        Initialize with the cart and a preconfigured pricing service with the registered rules per item
        :param cart:
        :param pricing_service:
        """
        self.cart = cart
        self.pricing_service = pricing_service

    def get_total(self):
        """
        this simple sums up the total amount for the individual items
        :return total_sum:
        """
        total_sum = 0

        for item in self.cart.values():
            item = self.pricing_service.apply_rule(item=item)
            total_sum = total_sum + item.total_price

        return total_sum
