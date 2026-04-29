
# Importing our logic file
import Day_20_logic

while True:
    print("\n, ~.~.~._Student Management system_.~.~.~")
    print("1. Add student")
    print("2. View all student")
    print("3. Search student")
    print("4. Exit")

    choice = input("Enter your choice(1-4): ")

    if choice == '1':
        name = input("Enter name: ")
        marks = input("Enter marks: ")
        result = Day_20_logic.add_stu(name, marks)
        print(result)

    elif choice == '2':
        # Calling the view function from logic file
        Day_20_logic.view_all()

    elif choice == '3':
        name = input("Enter name: ") 
        result = Day_20_logic.search_stu(name)
        print(result)
   
    elif choice == '4':
        print("GoodBye...")
        break