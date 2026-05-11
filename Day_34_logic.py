#--------Encapsulation (Data Security)------
#deine: It is the process of wrapping data (variables) and methods (functions) together and 
# restricting direct access to some components.

#Ye kyun zaroori hai?
#Socho agar aap kisi banking app mein code kar rahi ho. Agar koi user seedha aapka balance variable
# change kar sake (balance = 1000000), toh bank toh doob jayega!
#Encapsulation ka matlab hai: "Data ko private kar do aur bahar se usay seedha access mat karne do."

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
  # Double underscore (__) se variable 'Private' ban jata hai
        self.__balance = balance
  
  #method to check balance (read-only)
    def get_balance(self):
       return f"Your current Balance is: ${self.__balance}"
    

    #method to deposit (controlled access)
    def deposite(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited ${amount}"
        return "Invalid amount!"

