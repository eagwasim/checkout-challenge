class PricingService:
    """
    The PricingService handles registering different rules for items and applying the registered rules
    """

    def __init__(self):
        self.registered_rules = {}

    def register(self, item_name, rule):
        self.registered_rules[item_name] = rule

    def apply_rule(self, item):
        if item.code not in self.registered_rules.keys():
            return item

        self.registered_rules[item.code].apply(item)

        return item
