"""
_-----Data Cleaning (The Art of Handling Messy Data)-----_
 In the AI world, there is a golden rule: "Garbage In, Garbage Out." If your data has holes, missing values, or is unorganized, your AI model 
 will fail. Today, we learn how to "clean" the data before we ever use it.
   
  In real life, data is rarely perfect. Sometimes a price is missing, or a product category wasn't recorded. Pandas calls these "missing values" NaN (Not a Number).
We will use three power tools today:

    isnull():        Checks for missing data.

    fillna():        Fills in the blanks with a default value (like replacing a missing price with 0).

    sort_values():   Organizes the data in a specific order (like Price from low to high).
"""

import pandas as pd
import numpy as np

def get_crypto_data():
    # Defining a dictionary containe crypto coin data
    # 'np.nan' represents missing (Not a Number) data
    data = {
          'Coin': ['Bitcoin', 'Ethereum', 'Solana', 'Cardano', 'Dogecoin'],
          'Price_USD': [9500, 3500, np.nan, 0.5, 0.35],  # Solana has a missing price
          'Market_Cap_Billion': [1800, 400, 80, 40, 50]
}

# create a dataframe from a dictionary
    df = pd.DataFrame(data)
    return df





