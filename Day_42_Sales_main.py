from matplotlib import category
import pandas as pd
from Day_42_Sales_Logic import load_sales_data, get_category_summary

# Configuration: Show all columns clearly
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

# 1. Load data
sale_df = load_sales_data()
print(" --- Raw Sales Transaction ---")
print(sale_df)

# 2. Process Data: Generate Summary
# This transforms individual sales into category-wise totals
category_report = get_category_summary(sale_df)
print("\n --- Sales Summery By Category ---")

# 3. Export: Saving the summary report
category_report.to_csv('Day_42_Category_sales_report.csv', index=False)
print("\nSuccess: Category report has been exported!")


"""
--- DAY 42 SUMMARY ---
Today we mastered 'Data Aggregation'. 
Instead of looking at individual items, we used .groupby() to see the 
big picture. This is essential for creating business dashboards and 
financial reports where summarized totals are required.

"""

