import pandas as pd
from Day_39_logic import get_job_data, clean_job_data


# This tells Pandas to show every single column without hiding any
pd.set_option('display.max_columns', None)
# This increases the width of the display so columns don't wrap to the next line
pd.set_option('display.width', 1000)

# 1. Load the data from CSV
raw_df = get_job_data()
print("---- Raw Applicants List ----")
print(raw_df)


# 2. Clean the data (Handle missing values)
# Why: To make sure every candidate has a valid experience and salary number
df = clean_job_data(raw_df)

# 3. Filtering: Shortlist Python Developers with > 1 year experience
# This is like a real-world search query
python_devs = df[(df['Programming_Language'] == 'Python') & (df['Experience_Years']>1)]

print("\n--- Shortlisted Python Developers ---")
print(python_devs)

# 4. Sorting: Most experienced candidates at the top
df.sort_values(by='Experience_Years', ascending=False, inplace=True)

print("\n--- Applicants Ranked by Experience ---")
print(df)


"""
--- The Display Settings
pd.set_option('display.max_columns', None)---
   'set_option':             is a configuration tool.     
   'max_columns':            defines the limit.    
   'None':                   means infinity
   Logic: By default, Pandas hides columns in the middle if the table is wide. This line forces it to show every single column.

pd.set_option('display.width', 1000)---
   Logic: This expands the "printing area" of your terminal. It prevents the table from breaking into multiple lines, keeping it clean and readable.

    
 --- The "Power Filter" (The most important part)
python_devs = df[(df['Programming_Language'] == 'Python') & (df['Experience_Years'] > 1)]----

       df[...]:           This is the "Search Box".
      & (AND operator):   This is a strict rule. It tells Python that both conditions must be true at the same time.
      Logic: We are looking for candidates who are skilled in 'Python' AND have more than 1 year of experience. This is how HR departments shortlist candidates automatically.


 --- The Sorting Logic
 df.sort_values(by='Experience_Years', ascending=False, inplace=True)---
     by='Experience_Years':   Tells Pandas which column is the "Boss" for ranking.
     ascending=False:         This sets the order to Descending (Highest to Lowest).
     inplace=True:            This tells Python to "Save the changes permanently" in the same variable df rather than making a copy.

"""