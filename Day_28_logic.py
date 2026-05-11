# Searching in CSV Files
import csv

def search_stu(filename, search_name):
    with open(filename, mode="r") as f:
        reader = csv.reader(f)

        next(reader)

        for row in reader:
            if row[0].strip().lower() == search_name.strip().lower():
                return row
            
    return None