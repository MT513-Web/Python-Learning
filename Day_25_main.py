from unittest import result

import Day_25_logic

file_name = "my_notes.txt"

print("Your notes: ")
with open(file_name, "r") as f:
    print(f.read())


to_del = input("Which dp you want to del? (Write exact text) \n")
result = Day_25_logic.del_note(file_name, to_del)
print(result)