#~.~.Append Mode ('a').~.~

# with open("Day_22_daily_log.txt", "a") as file:
#     file.write("Adding another student: Amna\n")

# with open("Day_22_daily_log.txt", "r") as file:
#     for line in file:
#         print("Students details:", line.strip())


with open("Day_22_daily_log.txt", "a") as f:
  while True:
    learn = input("What d you learn today? (or type 'exit' to stop )\n")
    if learn == 'exit':
      break
    else:
      f.write(f"Good you have learned '{learn}'. \n")

with open("Day_22_daily_log.txt", "r") as f:
   lines = f.readlines()
   print(f"\nTotal entries in log file:{len(lines)}")