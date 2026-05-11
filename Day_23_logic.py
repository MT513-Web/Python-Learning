#Use of try and except----

def read_my_file(fileName):
   try:
     with open(fileName, "r") as f:
        return f.read()
     
   except FileNotFoundError:
      return "Error! File not found..."
   
   except Exception as e:
      return f"Somehting went wrong!!! {e}"


#Task...Daily expences list.....

def save_expences(itemName, price):
    with open("Day_23_expences.txt", "a") as f:
        f.write(f"Item Name: {itemName}, Price: {price} \n")
    return "Expences saved..."
    

def view_expences():
    try:
        with open("Day_23_expences.txt", "r") as f:
            return f.read()   
    except FileNotFoundError:
        return "Error! File not found..."