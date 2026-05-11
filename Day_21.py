#------File Handling------#

file = open("My_test_21.txt", "r")

# file.write("\n .~.~.File Handling.~.~.")
# file.write("\nSalam! This is our day 21.")
# file.write("\nThis is our file. \n")

# file.close()


content = file.read()
print(content)
file.close()

# uni_name = (input("Enter your university name: "))
# deg_name = (input("Enter your degree program: "))

# file.write("\n.~.~.Student Info.~.~. \n")
# file.write(f"Student study in {uni_name}. \n") 
# file.write(f"Degree of student is {deg_name}. \n")
# file.close