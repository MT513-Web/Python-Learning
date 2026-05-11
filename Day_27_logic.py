import csv

def read_st_data(filename):
    records =  []

    try:
        with open(filename, mode ="r") as f:
            reader = csv.reader(f)
            for row in reader:
                records.append(row)
        return records
    except FileNotFoundError:
        return "File not found!"
    