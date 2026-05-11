
import Day_28_logic

file_name = "Day_26_students_data.csv"


while True:
     search_student = input("\n Enter name of the student which do you want to search: (or 'exit' to stop) ")

     if search_student.lower() == 'exit':
          break
     result = Day_28_logic.search_stu(file_name, search_student)

     if result:
          print("\n Student Found!")
          print(f"Name: {result[0]} {result[1]}")
          print(f"Age: {result [2]}")
          print(f"Grade: {result [3]}")

     else:
          print("Sorry, student with this name not found!")