#OOP (Object-Oriented Programming)
#OOP lets you create a "Template" and then generate as many "Copies" (Objects) as you want.
#Class: This is your Blueprint or Cookie Cutter. It defines what a student should have (Name, Roll Number, CGPA).
#Object: This is the actual Cookie made from that cutter. Ayesha is an Object, your friend is an Object. 
# You both are "Students" (the Class), but your data (Name, CGPA) is different.

#Types of constructors 

#1. Default costructor
class Student:
    def __init__(self):
        self.name = "Unknown"
        self.cgpa = 0.0

ayesha = Student() # Default Constructor call hua
print(ayesha.name) # Output: Unknown

#Parameterized constructors
class Student:
    def __init__(self, name, cgpa):
        self.name = name
        self.cgpa = cgpa

a = Student("Ayesha", 3.36) # Parameterized Constructor call hua
print(a.name) # Output: Ayesha
print(a.cgpa)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Baaki languages (Java/C++) mein aap aik hi class mein multiple constructors bana sakti hain. Python mein
#  aisa nahi hota— agar aap aik se zyada __init__ likhengi, toh Python sirf aakhri wala consider karega.
#Lekin, Python ka Jugaar (Default Arguments):

#Python mein aap dono ka mixture bana sakti hain, jo exams mein bonus points dilwata hai:
class Students:
    # Yahan "Unknown" default value hai
    def __init__(self, name="Unknown", cgpa=0.0):
        self.name = name
        self.cgpa = cgpa

# Ab yeh dono kaam kar raha hai! 
s1 = Students() # Default behavior (Uses "Unknown", 0.0)
s2 = Students("Ayesha", 3.36) # Parameterized behavior
s3 = Students("Amna", 3.40)
print(s1.name, s1.cgpa)
print(s2.name, s2.cgpa)
print(s3.name, s3.cgpa)


#================================================================================
# logic.py
class Student:
    # __init__ is a special function called the "Constructor"
    # It runs automatically the moment we create an Object
    def __init__(self, name, cgpa, semester):
      self.name = name
      self.cgpa = cgpa
      self.semester = semester

      # This is a method (a function inside a class)
    def display_info(self):
         return f"Student: {self.name}, CGPA: {self.cgpa}, Semester: {self.semester}"
#======================================================================================    



