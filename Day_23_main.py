import Day_23_logic

file_name = input("Which file do you want to read?")

data = Day_23_logic.read_my_file(file_name)

print("\n*----Result----*")
print(data)




#Task...Daily expences list.....
while True:
 print("~.~.~. Expences Manager.~.~.~")
 print("1. Add Expense")
 print("2. View Expenses")
 print("3. Exit")

 choice = input("Enter choice (1 to 3): ")

 if choice == "1":
    item = input("Item Name: ")
    price = input("Price: ")
    result = Day_23_logic.save_expences(item, price)
    print(result)

 elif choice == "2":
    data = Day_23_logic.view_expences()
    print("~.~.~. Your Expences List~.~.~.")
    print(data)

 elif choice == "3":
    print("Your list is complteted...")
    break

