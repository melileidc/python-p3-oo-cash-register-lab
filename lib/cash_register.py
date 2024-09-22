#!/usr/bin/env python3

class CashRegister:

    def __init__(self, discount = 0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction = 0

    def add_item(self, title, price, quantity = 1):
        for i in range(quantity):
            self.items.append(title)

        self.last_transaction = price * quantity
        self.total += price * quantity

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
        else:
            self.total = round(self.total - (self.total * (self.discount / 100)))
            print(f"After the discount, the total comes to ${self.total}.")

    def void_last_transaction(self):
        self.total -= self.last_transaction

# takes one optional argument, a discount, on initialization.
# sets an instance variable total on initialization to zero. 
# accepts a title and a price and increases the total.
# also accepts an optional quantity.
# doesn"t forget about the previous total
# applies the discount to the total price.
# returns success message with updated total
# reduces the total
# returns a string error message that there is no discount to apply
# returns an array containing all items that have been added
# returns an array containing all items that have been added, including multiples
# subtracts the last item from the total
# returns the total to 0.0 if all items have been removed