class Item:
    """
    This is out domain! The item hold the details of its inventory item
    """

    def __init__(self, name, code, unit_price):
        self.name = name
        self.code = code
        self.quantity = 0
        self.unit_price = unit_price
        self.total_price = 0

    def increment(self):
        """
        We use the increment method so that the total price can be computed in real time
        """
        self.quantity = self.quantity + 1
        self.total_price = self.quantity * self.unit_price
