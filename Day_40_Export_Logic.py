#---------The Final CRUD Step - Exporting Data-------#
"""
In real professional work, after you clean and filter a huge dataset (like your job applicants), 
you don't just look at it in the terminal. You save it as a new, clean file to send to your manager or a client.

We will use your existing Job Applicant logic but add a new "Export" function.

"""

import pandas as pd

def get_job_data():
        # Load the dataset from CSV
        return pd.read_csv('Day_39_job_applicants.csv')


def clean_and_filter(df):
              """--- Clean missing values and filter for Python experts ---"""   
              # filling missing data 'Experience_Years' & 'Expected_Salary'
             
              df['Experience_Years'] =  df['Experience_Years'].fillna(0)
              avg_salary = df['Expected_Salary'].mean()
              df['Expected_Salary'] = df['Expected_Salary'].fillna(avg_salary)
  
              # Shortlisting logic
              Shortlisted = df[(df['Programming_Language'] == 'Python') & (df['Experience_Years'] > 1)]
              return Shortlisted


def save_to_file(df, filename):
              """---Save the processed DataFrame to a new CSV file---"""
              # 'to_csv' is the command that writes data back to your hard drive
              # index=False prevents pandas from adding an extra column of numbers
              df.to_csv(filename, index=False)
              return f"Successfully saved to {filename}"



"""
           ----df.to_csv('filename.csv', index=False)----

What: This command takes the table currently in Python's memory and "writes" it physically onto your computer's storage.

index=False: If you don't add this, Pandas adds a "0, 1, 2" column at the start of your CSV. Setting it to False keeps the file clean.

Why: This is the "Output" of your entire project. If you are building a tool for a company, they need this file to actually call the candidates.



Why a New File?

Logic: We never overwrite our original job_applicants.csv. We keep the original data safe and save our "Results" in a separate file. 
This is a best practice in Data Engineering.

"""



















