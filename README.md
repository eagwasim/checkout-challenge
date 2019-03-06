# Novicap Checkout Challenge

##### Besides providing invoice finance, NoviCap also runs a physical store which sells (only) 3 products:

``` 
Code         | Name                |  Price
-------------------------------------------------
VOUCHER      | NoviCap Voucher      |   5.00€
TSHIRT       | NoviCap T-Shirt      |  20.00€
MUG          | NoviCap Coffee Mug   |   7.50€
```
Various departments have insisted on the following discounts:

 * The marketing department believes in 2-for-1 promotions (buy two of the same product, get one free), and would like for there to be a 2-for-1 special on `VOUCHER` items.

 * The CFO insists that the best way to increase sales is with discounts on bulk purchases (buying x or more of a product, the price of that product is reduced), and demands that if you buy 3 or more `TSHIRT` items, the price per unit should be 19.00€.

Examples:

    Items: VOUCHER, TSHIRT, MUG
    Total: 32.50€

    Items: VOUCHER, TSHIRT, VOUCHER
    Total: 25.00€

    Items: TSHIRT, TSHIRT, TSHIRT, VOUCHER, TSHIRT
    Total: 81.00€

    Items: VOUCHER, TSHIRT, VOUCHER, VOUCHER, MUG, TSHIRT, TSHIRT
    Total: 74.50€
## Getting Started

Clone The Project

### Prerequisites

The project requires no external dependencies. Just a Runtime

```
Python 3.7
```
## Running the tests

Run the test cases using 

```
python3.7 test.py
```
## Challenge Author

* **Nicolas Overloop**

## License

This project is licensed under the MIT License

## Acknowledgments
* None

