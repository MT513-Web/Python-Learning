#--------Polymorphism (Many Forms)---------#
""" 'Poly'  means Many, and "morph" means Forms. Polymorphism allows different classes to be 
 treated as instances of the same general class through the same interface.

define:'''Polymorphism allows objects of different classes to be treated as objects of a common superclass, 
 allowing us to use a single interface for different types of objects'''
  
  Why are we doing this?
Imagine you are building a Payment System for an E-commerce site. 
 You have different payment methods: Credit Card, PayPal, and Crypto. 
 They all have a pay() function. When a user clicks "Checkout", your code shouldn't care which method they use. 
 It should just call pay() and let the object handle the details."""

class CreditCard:
    def process_payment(self, amount):
        return f"Processing credit card payment of ${amount} via bank gateway."

class Paypal:
    def process_payment(self, amount):
        return f"Processing paypal payment of ${amount} via secure token."

class Crypto:
    def process_payment(self, amount):
        return f"Processing crypto payment of ${amount} via blockchain."

