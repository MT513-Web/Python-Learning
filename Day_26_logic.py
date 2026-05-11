#-----CSV Files-----#
import csv

def setup_csv(filename):

    with open(filename, mode="w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["First_Name", "Last_Name", "Age", "Grade"])
    return "Headers Created!"

 
def save_stu_record(filename, first_name, last_name, age, grade):
    
    with open(filename, mode="a", newline="") as f:
        writer = csv.writer(f)

        writer.writerow([first_name, last_name, age, grade])
    
    return "Record successfuly saved in CSV!"
  