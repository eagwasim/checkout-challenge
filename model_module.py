class Item:
    def __init__(self, name, code, unit_price):
        self.name = name
        self.code = code
        self.quantity = 0
        self.unit_price = unit_price
        self.total_price = 0

    def increment(self):
        self.quantity = self.quantity + 1
        self.total_price = self.quantity * self.unit_price
