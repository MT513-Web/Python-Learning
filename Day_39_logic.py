#-----Professional CRUD with Pandas & CSV-------
"""
 What:    We created a Python-based Data Processing system that loads an external CSV file containing Job Applicant data.

Why:     In real-world Data Science, data is often "messy" (missing values). We used Pandas to clean this data (filling holes) and then used 
"Conditional Filtering" and "Multi-column Sorting" to find the best candidates.

"""


import pandas as pd

def get_job_data():
    # Loading the data from our local CSV file
    df = pd.read_csv('Day_39_job_applicants.csv')   # 'read_csv' turns the file into a DataFrame (df)
    return df


def clean_job_data(df):
    # Filling missing Experience with 0 and Salary with the average
    # We use fillna so the missing values don't break our calculations
    df['Experience_Years'] =  df['Experience_Years'].fillna(0)

    # Replace missing salary with the average salary of the group
    avg_salary = df['Expected_Salary'].mean()
    df['Expected_Salary'] = df['Expected_Salary'].fillna(avg_salary)

    return df

