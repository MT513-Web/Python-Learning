#Mini_Project_Personal_Contact_Book(Smart_Phonebook)

                         # --- SMART PHONEBOOK ---
contacts_info = {}

print("="*30)
print("  WELCOME TO SMART CONTACTS  ")
print("="*30)

for i in range(3):
    name = input(f"\n({i+1}) Contact Name: ").strip().lower()
    number = input("    Contact Number (11 digits): ").strip()

    if len(number) == 11:
      contacts_info[name] = number
      print(f"    {name.title()} has been saved.")
    else:
     print(" Error: Invalid number (Must be 11 digits).")
print("Your contact list is", contacts_info)

print("\n" + "-"*30)
print(f" YOUR DIRECTORY: {contacts_info}")
print("-"*30)

# --- SEARCH SECTION ---

search = input("\n Enter name to search: ").strip().lower()
if search in contacts_info:
   print(f" Result: {search.title()}'s number is {contacts_info[search]}")
else:
    print(f" '{search}' not found in contacts.")

# --- DELETE SECTION ---
remove = input("\n Which contact to delete? ").strip().lower()
if remove in contacts_info:
    del contacts_info[remove]
    print(f" {remove.title()} deleted successfully.")
else:
    print(" No such contact found.")
print()
print(f"Your updated contact list is: {contacts_info}")
print("\n" + "="*30)
print("   THANK YOU FOR USING APP   ")
print("="*30)
