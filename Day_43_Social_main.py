import pandas as pd
from Day_43_Social_Logic import load_social_data, process_dates, monthly_likes

# Configuration
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

# 1. Load Data
df = load_social_data()

# 2. Process Dates
# Converting strings to dates and extracting features
df = process_dates(df)
print ("--- Data With Extracted Date Feautres ---")
print(df)

# 3. Monthly Summary
monthly_report = monthly_likes(df)
print("\n--- Total Likes per Month ---")
print(monthly_report)

# 4. Export
monthly_report.to_csv('Day_43_Monthly_engagement_report.csv', index= False)
print("\nSuccessfully: Day 43 Engagement report exported!")




"""
--- pd.set_option('display.max_columns', None) & pd.set_option('display.width', 1000) ---

Why: As we discussed, this ensures that the terminal shows every column (Platform, Post_Date, Month, Day_of_Week) 
in one single, wide line instead of hiding them with ....

--- df = process_dates(df) ---
Why: This is the most important call. We send the raw data to the logic file, it adds the "Month" and "Day" columns, 
and sends (returns) the updated table back to us.
Crucial Note: If you don't write df =, the changes won't be saved in the Main file.

monthly_report = monthly_likes(df)
Why: Now that our table has a 'Month' column, we can calculate which month was the most successful.

--- monthly_report.to_csv('Day_43_monthly_engagement_report.csv', index=False) ---
Why: This creates the final physical file. The index=False ensures we don't get that annoying extra column of numbers (0, 1, 2, 3) in our CSV.
"""




"""
--- DAY 43 SUMMARY ---
Today we learned how to handle Date columns. By converting strings to 
'datetime' objects, we unlocked the ability to extract months and days, 
allowing us to perform 'Time-Series' summaries.
"""




