#Lists[]_vs_Tuples() & slicing
#Tuple change nahi hoti, is liye iske methods bohat kam hain:
#Accessing: Bilkul list ki tarah my_tuple[0] se item nikaal sakte hain.
#.count(item): Ye batata hai ke aik item kitni dafa aaya hai.
#.index(item): Ye batata hai ke item kis position par hai.

#making_grocery_list
grocery_list= ["milk", "sugar", "salt"]
shop_info = ("Abc Store", "Sahiwal", "26-3-25")

new_item = input("Which item you want to add?")
grocery_list.append(new_item)
print(grocery_list, "\n")

primary_item = input("Which item do you want to write at first?")
grocery_list.insert(0, primary_item)
print( "Updated_list:",grocery_list, "\n")

top_items = grocery_list[0: 2]
print("Top items:", top_items)

grocery_list.sort()

print("\n" ":======:Grocery_List:======:" "\n")
print( grocery_list, "\n")
print("Shop Name:", shop_info[0], "\n")

checking_item = input("Which item you want to check in list?")
if checking_item in grocery_list:
    print("Yes,", checking_item, "is in list.", "\n")
else:
    print("No,", checking_item, "is not in list.", "\n")
print(grocery_list, "\n")
