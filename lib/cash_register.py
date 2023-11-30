#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
      self.discount = discount
      self.total = 0
      self.items = []
      self.last_transaction_cost = 0  # New attribute to store the cost of the last transaction

    def add_item(self, title, price, quantity=1):
      self.cart = price * quantity
      self.total += self.cart
      for i in range(quantity):
        self.items.append(title)
        
        
      self.last_transaction_cost = self.cart

    def apply_discount(self):
      if self.discount > 0:
        discount_percent = (100 - self.discount) / 100
        self.total = int(self.total * discount_percent)
        print(f'After the discount, the total comes to ${self.total}.')
      else:
        print('There is no discount to apply.')

    def void_last_transaction(self):
        
     self.total -= self.last_transaction_cost
