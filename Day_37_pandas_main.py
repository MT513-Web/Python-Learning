from Day_37_pandas_logic import get_inventory_data

#loading the inventry
# 'df' is our Excel sheet (DataFrame)
df = get_inventory_data()

# Check what columns Pandas actually loaded
print("Columns found in your data:", "\n",  df.columns)

#view whole inventry
print("-----Tech Inventory-----")
print(df)


# [1] Accessing a column and filtering
# Logic: Look into 'df', find the 'Category' column, check if it matches 'Computing'
print("\n ~=== Computing Products Only ===~ ")
computing_gear = df[df['Category'] == 'Computing']
print(computing_gear)

# [2] The "Tool" called Method
# Logic: Go to 'Price' column and calculate the average automatically
print ("\n ~=== Average Price of the Products ===~ ")
avg_price = df['Price'].mean()
print(f"Average Price: {avg_price}")

