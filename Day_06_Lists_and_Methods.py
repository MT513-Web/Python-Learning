#Python Lists (Collecting Data) 
#.append(item), .insert(index, item), .remove(item), .sort(), len(list)
#_Uses_in_real_life_1. WhatsApp & Messenger (Chat Lists),2. YouTube & Netflix (Playlists)
#3. Contacts in Phone,4. Online Shopping (Amazon/Daraz)

cart = []
item1 = input("Enter your item1:")
cart.append(item1)

item2 = input("Enter your item2:")
cart.append(item2)

item3 = input("Enter your item3:")
cart.append(item3)

print(f"Your list contains 3 items {cart}.")

remove_items = input("Which items you want to remove?")
cart.remove(remove_items)
cart.sort()
print(f"Final list (A to Z): {cart}")


#2nd_method_Loop Method (The "Pro" Way)
cart = []
for i in range(3):
    item = input(f"Write your item {i+1}: ").strip().lower()
    cart.append(item)

print(f"Your list contains 3 items {cart}.")

remove_item = input("which item you want to remove?").strip().lower()
if remove_item in cart:
    print(f"Done! '{remove_item}' has beem removed.")
else:
    print(f"Sorry, '{remove_item}' is not in your cart.")

cart.remove(remove_item)
cart.sort()
print(f"Yor final list is (A to Z): {cart}")
