
# List to store student records as dictionaries
student_list = []
"""Adds a new student to the list."""
def add_stu(name, marks):
     new_stu = {"n" : name, "m": marks}
     student_list.append(new_stu)
     return f"{name} has been added!"


def view_all():
     """Displays all students currently in the list."""
     if not student_list:
          print("List is empty...")
     else:
          for s in student_list:
               print(f"Name: {s['n']}, Marks: {s['m']}")


def search_stu(name):
     """Searches for a student by name (case-insensitive)."""
     for s in student_list:
        if s['n'].lower() ==name.lower():
          return f"Found! Name: {s['n']}, Marks: {s['m']}"
     return "Sorry, student not found"
          