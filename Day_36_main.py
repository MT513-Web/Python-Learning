
from Day_36_logic import apply_discount, InvalidDiscountError

price = 1000
discount = 200 # Intentionally invalid discount value

try:
    # attempt to apply discount
    result = apply_discount(price, discount)
    print (f"Final Price {result}")

except InvalidDiscountError as e:
    # Catch and display the custom error message
    print(f"Caught an error: {e}")

