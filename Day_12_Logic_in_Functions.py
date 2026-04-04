# Logic_&_Conditions_inside_Functions
#Smart Weather Assistant, Grade System 
#Smart Weather Assistant (If-Else inside Function)
def check_weather(temp):
    if temp >= 35:
        print("It's summer...")
    elif temp >= 20 and temp <= 35:
        print("It's cool weather...")
    else:
        print("It's cold...")

user_temp = int(input("Enter current temperature:"))
result = check_weather(user_temp)

#Checking_Even_Odd
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
    
num = int(input("Enter number:"))
if is_even(num):
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")


#for_many_inputs
def is_even(number):
    return number % 2 == 0

print("--- Even/Odd Checker (Type '0' to exit) ---")

while True:
    user_input = input("\nEnter a number: ")
    
    # Check if user wants to quit
    if user_input == '0':
        print("Program is ending!")
        break
    
    try:
        num = int(user_input)

        if is_even(num):
            print("Even number")
        else:
            print("Odd number")

    except ValueError:
        print("Invalid input! Please enter a number.")


#Grade System 
def calculate_grade(marks):
    if marks < 0 or marks > 100:
       return "Error! Please enter valid marks."
    elif marks >=90:
      return "Grade A+"
    elif marks >= 80:
       return "Grade A"
    elif marks >=70:
       return "Grade B"
    elif marks >= 60:
       return "Grade C"
    elif marks >=50:
       return "Grade D"
    else:
       return "Grade F"
    
student_marks = int(input("Enter your marks:"))
result = calculate_grade(student_marks)
print(result)
