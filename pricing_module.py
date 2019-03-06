class PricingService:
    def __init__(self):
        self.registered_rules = {}

    def register(self, item_name, rules):
        self.registered_rules[item_name] = rules

    def apply_rule(self, item):
        if item.code not in self.registered_rules.keys():
            return item

        self.registered_rules[item.code].apply(item)

        return item
