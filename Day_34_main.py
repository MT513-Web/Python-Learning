from Day_34_logic import BankAccount

# Creating an account
my_account = BankAccount("Ayesha", 5000)

#Use the method to check balance
print(my_account.get_balance())

#Use the method to deposit money
my_account.deposite(200)
print(my_account.get_balance())



#TEST: Try to break the security (The Error Test)
# Uncomment the line below to see what happens when you try to hack the private variable:
# print(my_account.__balance)