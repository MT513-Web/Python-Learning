"""
--- Comprehensive Data Analytics Project ---
What?
We are acting as Data Analysts for a Store. 
We will:
"Merge" sales data with product information.
"Clean" missing values.
"Process Dates" to see which month performed best.
"Calculate" total profit.
"Group" the data to see the top-performing category.

Why?
This is a real-world simulation. In a real job, you don't just do "one" thing; you perform a series of steps to turn raw files 
into a business report. This project proves you are ready for a junior data role.

"""

import pandas as pd

def load_and_merge():
    """Step 1: Load and combine datasets using a common ID."""
    df_prod = pd.read_csv('Day_45_master_products.csv')
    df_sales = pd.read_csv('Day_45_master_sales.csv')
    # Joining the Product info (Cost) with Sales info (Price/Units)
    return pd.merge(df_prod, df_sales, on='ID', how='inner')

def clean_and_calculate_data(df):
    """Step 2: Data Cleaning and Feature Engineering"""
    # Filling missing units with 0 so the math doesn't break
    df['Units_Sold'] = df['Units_Sold'].fillna(0)

    # Calculating Total Revenue and Total Cost
    df['Total_Revenue'] = df['Units_Sold'] * df['Selling_Price']
    df['Total_Cost'] = df['Units_Sold'] * df['Cost_Price']
    # Calculating Profit
    df['Profit'] = df['Total_Revenue'] - df['Total_Cost']

    # Data Proccessing: Extracting Month from Date
    df['Sale_Date'] = pd.to_datetime(df['Sale_Date'])
    df['Month'] = df['Sale_Date'].dt.month
    
    return df

def get_final_summary(df):
    """Step 3: Aggregating data for the final Business Report"""
    # Grouping by Category to see which department is most profitable
    summary = df.groupby('Category').agg({
         'Profit': 'sum',
          'Units_Sold': 'sum',
          'Total_Revenue': 'sum' # Adding average revenue per sale for extra detail
     }).reset_index()       
     
     # Rename for clarity
    summary.rename(columns={'Total_Revenue': 'Avg_Sale_Value'}, inplace=True)
    return summary.sort_values(by='Profit', ascending=False)



"""
--- pd.merge(df_prod, df_sales, on='ID', how='inner') ---
Logic: Uses the 'ID' column as a bridge to glue product info (Cost) and sales info (Price) into one table.

--- df['Units_Sold'].fillna(0) ---
Logic: Finds empty cells in sales and puts a '0' so the upcoming math doesn't crash.

--- df['Total_Revenue'] = df['Units_Sold'] * df['Selling_Price'] ---
Logic: Calculates total money earned from customers.

--- df['Total_Cost'] = df['Units_Sold'] * df['Cost_Price'] ---
Logic: Calculates how much the store spent to buy those items.

--- df['Profit'] = df['Total_Revenue'] - df['Total_Cost'] ---
Logic: Subtracts cost from revenue to find the actual earnings.

--- pd.to_datetime(df['Sale_Date']) ---
Logic: Changes the date from "Text" to a "Smart Object" that Python understands.

--- df['Sale_Date'].dt.month_name() ---
Logic: Extracts the name (e.g., March) from the date object.

--- df.groupby('Category').agg({'Profit': 'sum', 'Units_Sold': 'sum'}) ---
Logic: Piles up all items by category and adds up their total profit and total units sold.


"""

