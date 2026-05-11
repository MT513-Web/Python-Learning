from Day_35_logic import CreditCard, Crypto, Paypal

#list of diff payment methods
payment_methods = [CreditCard(), Paypal(), Crypto()]

# We don't care WHICH object it is, we just call the same method!
for method in payment_methods:
    print(method.process_payment(100))




"""Flexibility: 
 If you want to add a new payment method tomorrow (e.g., ApplePay), you just create the class, 
add it to the list, and your main.py code doesn't need to change at all. 
 This is called "Open-Closed Principle" in professional software design."""



