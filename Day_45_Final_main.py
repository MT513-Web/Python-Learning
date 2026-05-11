import pandas as pd
from Day_45_Final_Logic import load_and_merge, clean_and_calculate_data, get_final_summary

# Display settings for better readability
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

# 1. Ingestion & Merging
combined_data = load_and_merge()

# 2. Cleaning & Feature Engineering
processed_data = clean_and_calculate_data(combined_data)
print("--- Detailed Processed Data ---")
print(processed_data)

# 3. Final Summary Report
final_report = get_final_summary(processed_data)
print("--- Final Summary Report ---")
print(final_report)

# 4. Exporting the final report to a CSV file
final_report.to_csv('Day_45_Final_Summary_Report.csv', index=False)
print("Final summary report has been exported to 'Day_45_Final_Summary_Report.csv'.")


"""
--- DAY 45 GRADUATION SUMMARY ---
This project represents the complete Data Science lifecycle:
1. MERGE: Joined product details with sales records.
2. CLEAN: Handled null values in units.
3. DERIVE: Created 'Profit' and 'Month' columns.
4. ANALYZE: Summarized profit by business category.

* This final project demonstrates my ability to take raw data, perform necessary transformations, and produce actionable business insights.
* This is the kind of work I will be doing in a junior data role, and I'm now fully prepared to hit the ground running in my data career.

"""



