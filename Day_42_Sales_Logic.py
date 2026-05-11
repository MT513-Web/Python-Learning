#-----------Data Aggregation (Summarizing Data)---------#
"""
What are we doing today?
We are going to take a dataset of "Sales Transactions" and group them to see the total performance of different categories. 
For example, finding out the total sales for "Electronics" vs. "Clothing".


Why are we doing this?
In professional Data Science, managers don't want to see every single row of data. They want a Summary. 
The .groupby() function in Pandas is the most powerful tool to turn thousands of rows into a simple summary table.

"""

import pandas as pd

def load_sales_data():
    """ Load the sales dataset from CSV """
    return pd.read_csv('Day_42_sales_data.csv')

def get_category_summary(df):
    """Group the data by Category and calculate the total amount for each."""
    # Logic: .groupby('Category') gathers all rows of the same category together.
    # .agg({'Amount': 'sum'}) calculates the total sum for the 'Amount' column.
    summary = df.groupby('Category').agg({'Amount': 'sum'}).reset_index()

    # Sorting the summary so the highest-selling category is at the top
    summary = summary.sort_values(by='Amount', ascending=False)
    return summary



"""
  --- df.groupby('Category') ---
What: It tells Pandas to find all unique names in the "Category" column (Electronics, Clothing, etc.) and group their related rows together.
Why: This is like sorting your laundry; you put all shirts in one pile and all socks in another.

  --- .agg({'Amount': 'sum'}) ---
What: .agg stands for Aggregate. It performs a math operation on the group.
Why: We are telling Pandas: "Once you have the piles ready, add up all the numbers in the 'Amount' column for each pile."

  --- .reset_index() ---
What: When you group data, Pandas changes the structure. reset_index() makes it look like a normal, flat table again.
Why: It makes the output easier to read and easier to export to a clean CSV.

"""