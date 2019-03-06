from copy import copy

from finance_module import Checkout
from input_module import parse_input
from model_module import Item
from pricing_module import PricingService
from rules_module import TwoForOne, BulkPurchase


def start_program():
    pricing_service = get_pricing_service()

    inventory = get_inventory()

    print("Welcome no NoviCap!")
    print("Here is a list of our inventory")
    print("Name", " | ", "Code", " | ", "Unit Price")

    for inventory_item in inventory.values():
        print(inventory_item.name, " | ", inventory_item.code, " | ", inventory_item.unit_price)

    print("Please add to cart using the inventory code. eg. VOUCHER, TSHIRT, VOUCHER, VOUCHER, MUG, TSHIRT, TSHIRT")

    raw_arguments = input("Enter Items: ")

    while raw_arguments.upper() != "EXIT":
        try:
            cart = {}

            parsed_arguments = parse_input(raw_arguments)

            for parsed_argument in parsed_arguments:

                if parsed_argument not in cart:
                    cart[parsed_argument] = copy(inventory[parsed_argument])

                cart[parsed_argument].increment()

            checkout = Checkout(cart, pricing_service)

            print("Items: " + ", ".join(parsed_arguments))
            print("Total: {:.2f}".format(checkout.get_total()))

        except:
            print('PLEASE ENTER VALID COMMA SEPARATED ARGUMENTS\nVALID ARGUMENTS INCLUDE: VOUCHER, TSHIRT, MUG')

        raw_arguments = input("Enter Arguments: ")


def get_pricing_service():
    pricing_service = PricingService()

    pricing_service.register("VOUCHER", TwoForOne(discount=1.0 / 2.0))
    pricing_service.register("TSHIRT", BulkPurchase(discount=1.0 / 20.0))

    return pricing_service


def get_inventory():
    return {
        "VOUCHER": Item(name="NoviCap Voucher", code="VOUCHER", unit_price=5.00),
        "TSHIRT": Item(name="NoviCap T-Shirt", code="TSHIRT", unit_price=20.00),
        "MUG": Item(name="NoviCap Coffee Mug", code="MUG", unit_price=7.50)
    }


if __name__ == "__main__":
    start_program()
