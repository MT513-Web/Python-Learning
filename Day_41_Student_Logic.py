

#-----------Student Performance Analytics------------#
"""
we are going to work on a Student Performance Tracker. This is perfect because it relates to your university life and uses 
the exact Input -> Process -> Output pattern you want to master.

What are we doing today?
     We are creating a system to process student exam results. We will load a list of students, calculate their total marks, filter 
     out those who failed, and save the list of "Passing Students" into a new file.

     
Why are we doing this?
    In Data Science, we often need to create Derived Columns (columns created from other columns, like adding marks together). 
    This project will teach you how to do math across columns and how to perform a final export of filtered data.

"""

#  This file handles the data loading, cleaning, and the math for "Total Score."
import pandas as pd

def get_studenst_data():
    """Load the student result data from a CSV file."""
    return pd.read_csv('Day_41_student_results.csv')

def process_result(df):
    """Clean data and calculate performance metrics."""

    # Step 1: Fill missing scores with 0
    df['Math_Score'] = df['Math_Score'].fillna(0)
    df['English_Score'] = df['English_Score'].fillna(0)

    # Step 2: Create a 'Total_Score' column (Math + English)
    # This is a Derived Column
    df['Total_score'] = df['Math_Score'] + df['English_Score']
   
    # Step 3: Filter students who scored more than 100 in total (Passing)
    passing_students = df[df['Total_score'] >= 100]
  
    return passing_students


def export_passing_list(df, filename):
    """Save the filtered list to a new CSV file.""" 
    df.to_csv(filename, index=False)
    return f"File Saved Successfully as {filename}"








