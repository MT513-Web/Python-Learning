from unittest import result

import Day_26_logic

file_name = "Day_26_students_data.csv"

print(Day_26_logic.setup_csv(file_name))

while True:
    first_name = input("Enter First Name: ")   
    last_name = input("Enter Last Name: ")  
    st_age = input("Enter your age: ")   
    st_grade = input("Enter Grade: ")


    result = Day_26_logic.save_stu_record(file_name, first_name, last_name, st_age, st_grade)
    print(result)

    stop = input("Exit? (y/n): ")
    if stop.lower() == 'y':
        break