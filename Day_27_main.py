import Day_27_logic

file_name = "Day_26_students_data.csv"

all_records = Day_27_logic.read_st_data(file_name)

if isinstance(all_records, list):
    print("\n" + "="*50)
    print(f"{'First Name': <15} {'Last Name': <15} {'Age': <10} {'Grade': <10}")
    print("\n" + "="*50)
    for row in all_records[1:]:
        print(f"{row[0]: <15} {row[1]:<15} {row[2]:<10} {row[3]:<10}")
    print("\n" + "="*50)
else:
    print(all_records)