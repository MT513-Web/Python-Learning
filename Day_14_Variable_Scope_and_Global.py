#Day 14: Scope (Local vs Global Variables)

x = 5 #Global
def my_fun():
    y = 7#Local
    print(x)
    print(y)

my_fun()
print(x)
# print(y)#will generate an error

 # Day 14 Task: The Secret Keeper
company_name = "Ayesha Tech"
def employee_name():
 name = "Ayesha"
 print(company_name)
 print(employee_name)

employee_name()
print(employee_name)
print(company_name)#will generate an error


#fixing the error
company_name = "Ayesha Tech"

def employee_name():
   name = "Ayesha"
   return name

result = employee_name()
print(result)
print(company_name)


#Day 14: The Global Modifier Challenge 
#Task: The Bank Balance Tracker
balance = 1000
def deposit(amount):
     global balance
     balance += amount
     print(f"Deposited: {amount}")

deposit(500)
print(f"Final Balance: {balance}")

#The "Access Denied" System 
is_logged_in = False
def login():
    global is_logged_in
    is_logged_in = True

def view_profile():
    if is_logged_in == True:
      print("...welcome...")
    else:
     print("Access denied! Please login first.")

view_profile()
login()
view_profile()                            
