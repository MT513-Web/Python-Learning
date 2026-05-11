
"""
--- Data Merging (Connecting Different Files) ---
What?
We are going to learn how to Merge two separate CSV files. Imagine you have one file with Product Names and another file with Sales Prices. 
Instead of manually typing them, we will use Python to join them together using a common "Product_ID".

Why?
In the real world, data is rarely in just one file. Customer info is in one place, and their orders are in another. 
The pd.merge() function is the "glue" that brings them together so you can see the full picture.

"""

import pandas as pd

def load_data():
    """Load both product and price datasets"""
    products = pd.read_csv('Day_44_products.csv')
    prices  = pd.read_csv('Day_44_prices.csv')
    return products, prices


def merge_datasets(df_prod, df_price):
    """Combine two DataFrames into one using Product_ID"""
    # Logic: pd.merge looks for the 'Product_ID' in both files and matches them.
    # 'on' tells it which column is the common bridge.
    # 'how=inner' ensures it only keeps items that exist in both files.
    combined_df = pd.merge(df_prod, df_price, on='Product_ID', how='inner')
    return combined_df

def calculate_inventory_value(df):
    """Calculate the total value of stock for each product"""
    # Logic: Multiplying Price by Stock to create a new column
    df['Total_Stock_Value'] = df['Price'] * df['Stock']
    return df 



"""
--- pd.merge(df_prod, df_price, on='Product_ID') ---
What: It looks at the Product_ID column in both files. If it finds "101" in both, it puts all the info (Name, Category, Price, Stock) 
into one single row.
Why: This saves you from having to look back and forth between two different files.

df['Price'] * df['Stock']
What: It performs multiplication across columns from different original sources.
Why: To get the total worth of your inventory.

"""







