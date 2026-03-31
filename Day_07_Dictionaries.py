#_Python_Dictionaries_(Data with Meaning)
#Dictionary asal mein Database ki choti shakal hai.
#Contacts App: Name (Key) -> Phone Number (Value).
#Login Systems: Username (Key) -> Password (Value).
#Game Inventory: Weapon Name (Key) -> Damage Power (Value)

# Dictionary: {Key : Value}
fruits_prices = {
     "apple": 250,
     "bananas": 200,
     "mango": 300 
}
print(fruits_prices["apple"])

fruits_prices["cherry"] = 400 #for_add_more_things
print(fruits_prices["cherry"]) 

#-------------------------------------------------#
items = {} #an_empty_dictionary
for i in range(3):
    name = input("Item name:").strip().lower()
    price = int(input("Item price:"))

    items[name] = price
print("Your list is", items)

require_item = input(f"which item do you want?").strip().lower()

if require_item in items:
 item_price = items[require_item]
 print(f"The price of {require_item} is {item_price}.")
else:
   print("Not found")
