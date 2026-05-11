import pandas as pd
from Day_44_Merge_Logic import load_data, merge_datasets, calculate_inventory_value

# Configuration
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

# 1. Load Data: Getting two separate tables
df_products, df_prices = load_data()

# 2. Merge Data: Connecting them into one big table
# This is like a puzzle where pieces are matched by Product_ID
merged_df = merge_datasets(df_products, df_prices)

# 3. Process: Adding a new calculation
final_df = calculate_inventory_value(merged_df)

print("--- Final Merged Inventory Report ---")
print(final_df)

# 4. Export
final_df.to_csv('final_inventory_report.csv', index=False)
print("\nSuccess: Day 44 Merged report exported!")




"""
--- DAY 44 SUMMARY ---
Today we mastered 'Data Merging'. 
We used the .merge() function to combine two separate CSV files 
based on a common 'Product_ID'. This allows us to perform 
cross-file analysis, such as calculating 'Total_Stock_Value' 
using prices from one file and stock levels from another.
"""


