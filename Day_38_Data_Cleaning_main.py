
from Day_38_Data_Cleaning_logic import get_crypto_data

# Load the raw dataset from the logic file
df = get_crypto_data()

# Step 1: Inspect the data
# Print the raw data to see where the 'NaN' values are located
print("--- Raw Data With Missing Values ---")
print(df)

# Step 2: Cleaning the Data
# Calculate the average price of the existing coins
avg_price = df['Price_USD'].mean()
print (f"\n Average Price: {avg_price}")

# Fill the missing 'NaN' values with the calculated average
# This ensures we don't have empty holes during math operations
df['Price_USD'] = df['Price_USD'].fillna(avg_price)

print(f"\n Data Cleaned: Missing values filled with average ({avg_price:.2f})")
# Step 3: Sorting the Data
# Sort the DataFrame by Market Cap in descending order (highest to lowest)
# 'ascending=False' ensures the largest coins appear at the top
# 'inplace=True' applies the changes directly to our 'df' variable
df.sort_values(by='Market_Cap_Billion', ascending=False, inplace=True)


print("\n--- Sorted Data: Largest coins by Market Cap ---")
print(df)



"""      
      
df['Price_USD']:                   "Look only at the column named Price_USD."
.mean():                           "This is a built-in calculator. Add all the numbers in this column and divide them by the count."
Result:                             avg_price mein poori market ka average price (maslan 19000.5) save ho gaya


df['Price_USD'].fillna(avg_price):   "Find all the 'NaN' (holes/missing data) in the Price_USD column and fill them with the avg_price we just calculated." 
df['Price_USD'] = ...:               "Update the original column with this new cleaned version."


sort_values:                          "Rearrange the rows of this table."
by='Market_Cap_Billion':              "Look at the Market Cap column to decide who comes first."
ascending=False:                      "Don't go from small to big. Go from Big to Small (Highest Market Cap at the top)."
inplace=True:                         "Don't make a new table. Just shuffle the rows in this same df permanently."


"""