#Multiple_Returns,Multiple_Results,Default Arguments
def rectangle_info(length, width = 5):
  Area = (length * width)
  perimeter = 2 * (length+width)
  return Area, perimeter
 
length = int(input("Enter length:"))
width =  int(input("Enter width:"))
Area_result, perimeter_result = rectangle_info(length , width)
print(f"Area of rectangle is {Area_result}.")
print(f"Peremiter of rectangle is {perimeter_result}.")




#The Smart Billing System
def calculate_bill(price, quantity, tax_rate=18):
    subtotal = quantity * price
    tax_amount = subtotal * (tax_rate / 100)
    total_bill = subtotal + tax_amount
    return subtotal, tax_amount, total_bill

price = int(input("Enter price:"))
quantity = int(input("Enter quantity:"))
subtotal, tax, total = calculate_bill(price, quantity)
print(f"subtotal: {subtotal}.")
print(f"Tax amount: {tax}.")
print(f"Total bill: {total}")
