from random import choice
from unittest import result

import Day_24_logic

file_name = "my_notes.txt"
status = Day_24_logic.check_or_creat_file(file_name)
print(status)

while True:
    print("\n 1. Add note  2. Exit")
    choice = input("Choice: ")
    if choice == "1":
        fileName = input("Which file do you want to read? ")
        note = input("Write note: ")
        result = Day_24_logic.add_note(fileName, note)

    else:
        print("Exit")
        break