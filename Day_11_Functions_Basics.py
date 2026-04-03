#_Data_Structures_&_Functions
#_By_using_print
def greetings():
     print("Salam Girl!")
greetings()

#_By_using_return_then_print
def myFunction():
     return "It's my fun!"
print(myFunction())

#Adding_num
def add_numbers(num1, num2):
    return (num1 + num2)
print(add_numbers(4, 5))

#_further_use_
def multiply(a, b):
     return (a * b)
result = multiply(10, 4)
final_result = 100 - result
print(final_result)

#_Multiple_Parameters
def intro(name, age, city):
     print(f"My name is {name}. I am {age} years old. I live in {city}.")
intro("Ayesha", "22", "Sahiwal")

#Square
def calculte_square(number):
    return number * number
val = int(input("Enter number for squre:"))
result = calculte_square(val)
print(f"The square of {val} is {result}.")

#discount
def get_discount(amount):
    discount = amount * 0.1
    return amount - discount
Amount = int(input("Enter your amount:"))
result = get_discount(Amount)
print(f"Original price is: {Amount}")
print(f"Price at 10% discount is: {result}")



