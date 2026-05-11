import pandas as pd
from Day_41_Student_Logic import get_studenst_data, process_result, export_passing_list


# Configuration: Ensure all columns are visible in the terminal
pd.set_option('display.max_column', None)
pd.set_option('display.width', 1000)

# 1. Load Data
raw_data = get_studenst_data()
print(" \n ------- Raw Student Data -------")
print (raw_data)

# 2. Process Data (Clean + Math + Filter)
# We are calculating totals and filtering for passing students
passed_df = process_result(raw_data)

print("\n==== Passing Students (Total Score >= 100) ====")
print(passed_df)

# 3. Export Data
# Saving the result to a new file
message = export_passing_list(passed_df, 'Day_41_passed_students.csv')
print("\n" + message)





"""
     --- df['Total_Score'] = df['Math_Score'] + df['English_Score']---
       What: This tells Pandas to take the value of Math and English for each row, add them, and put the result in a brand new column.
       Why: In Data Science, we often need to combine multiple data points to get a final "Score" or "Rank."

     --- df.to_csv(filename, index=False) ---
       What: It writes the current table into a physical file on your laptop.
       Why: So you can open the results in Excel or email the "Passed Students" list to a teacher without needing to run Python.
 
     --- fillna(0) ---
       What: It replaces empty spots with zero.
       Why: If a student missed an exam, their score is missing. You cannot add "95 + Empty". You must turn "Empty" into "0" so the math works.


"""


"""
--- DAY 41 SUMMARY ---
Today we implemented a 'Calculation Logic' where we added two columns together 
to create a new 'Total_Score' column. We then used this new data to filter 
and export a specific group (Passing Students). This is a common workflow 
for automated grading or performance reporting systems.

"""


