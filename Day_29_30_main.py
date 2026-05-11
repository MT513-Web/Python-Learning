from calendar import Day
from random import choice

import Day_29_30_logic

file = "Day_29_30_Library_Data.csv"

while True:
    print("\n" + "~." *30)
    print(" E-Library Manager ")
    print("\n" + "~." *30)
    print("1. Add New Book")
    print("2. View All Books")
    print("3. Search by Title")
    print("4. Delete Book")
    print("5. Exit")

    choice = input("\n Select an option(1-5): ")

    if choice == '1':
        t = input("Enter Book Title: ") 
        a = input("Enter author name: ")
        s = "Available"
        p = input("Enter Price: ")
        print(Day_29_30_logic.add_book(file, t, a, s, p))

   
    elif choice == '2':
        records = Day_29_30_logic.get_all_books(file)
        print(f"\n {'Title':<20} {'Author':<20} {'Status': <20} {'Price': <10}")
        print("-"*70)
        for row in records[1:]:
            print(f"{row[0]:<20} {row[1]:<20} {row[2]:<20} {row[3]:<20}")
        print("-"*70)
   
    elif choice == '3':
       search_t = input("Enter book title to search: ")
       found = Day_29_30_logic.search_book(file, search_t)
       
       if found:
        print("\n Book Found...")
        print(f"Title: {found[0]}")
        print(f"Author: {found[1]}")
        print(f"Status: {found[2]}")
        print(f"Price: {found[3]}")
       
       else:
          print(f"\n {search_t} not found in your Library!") 

    elif choice == '4':
       del_t = input("Which book do you want to delete? ")
       confirm = input("Are you sure you want to delete '{del_t}'? y/n: ")
       if confirm.strip().lower() == 'y':
          print(Day_29_30_logic.del_book(file, del_t))

    elif choice == '5':
      print("GOOD BYE...")
      break
