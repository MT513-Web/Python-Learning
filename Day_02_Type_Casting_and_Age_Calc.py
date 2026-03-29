name = input("Enter your name:")
print("*" *10)
print("Welcome to Day 2", name)
print("*" *10, "\n")

#int>>>>>>>>>
num1 = int(input("First num:"))
num2 = int(input("Second num:"))
print(num1 + num2)

#float>>>>>>>.
num1 = float(input("First num:"))
num2 = float(input("Second num:"))
print("Result of addition is:", num1 + num2)
print("\n", "*" *10)
print("Result of multiplication is:", num1*num2)
print("\n", "*" *10)
print("Result of subtraction is:", num1-num2)
print("\n", "*" *10)
print("Result of division is:", num1/num2)
print("\n", "*" *10)


# age-calculation_1st_method
birth_year_input = int(input("Enter your birth year: "))
current_year = 2026
age = current_year - birth_year_input
print("*" * 30)
print("Great! Your age is ", age, "years.")
print("*" * 30)

#2nd_method
age = 2026 - int(input("Enter your birth year:"))
print("Your age is", age, "years.")
