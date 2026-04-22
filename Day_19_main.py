#_-_-_The Shortcut to Efficiency (Modules)_-_-_#
#main.py
import Day_19_logic

print(Day_19_logic.Welcome("Ayesha"))

print(Day_19_logic.power(3))



import random
from Day_19_logic import check_guess


guess = int(input("Enter your guessing number."))
secret = random.randint(1, 100)

result = check_guess(guess, secret)
print(result)