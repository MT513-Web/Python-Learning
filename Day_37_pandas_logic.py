""" ---------Pandas------
If Python is the brain of your projects, Pandas is the memory. It is the tool that allows you to read, analyze, 
and clean massive datasets (like Excel/CSV files) in seconds. Every AI model you build in the future will first require you to "Pandas" the data.

Introduction to Pandas
Think of Pandas as "Excel on steroids." While Excel crashes if you have a million rows, Pandas can handle millions of rows of data with ease.

Core Concepts
Series: A 1D array (like a single column in an Excel sheet).

DataFrame: A 2D table (like the entire Excel sheet with rows and columns)


What is Pandas really?
Socho tumhare paas Excel ki aik sheet hai.
Row: Aik specific gadget (e.g., Laptop).
Column: Us gadget ki property (e.g., Price, Stock, Category).
df (DataFrame): Yeh tumhari poori Excel sheet ka naam hai.
"""

import pandas as pd

def get_inventory_data():
    # data: A dictionary representing tech products
    data = {
        'Product': ['Laptop', 'Smartphone', 'Headphones', 'Monitor', 'Tablet'],
        'Price': [70000, 40000, 1000, 5000, 10000],
        'Stock': [10, 5, 8, 9, 7],
        'Category': ['Computing', 'Mobile', 'Audio', 'Computing', 'Computing'] 
} 

  # Converting dictionary to a Pandas DataFrame
    df = pd.DataFrame(data)
    return df



