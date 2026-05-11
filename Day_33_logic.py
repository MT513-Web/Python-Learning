#------Inheritance---------
#Why are we doing this? (The "Why")
#Imagine you are building a system for your university. You have 10 types of students:
#  CS Students, Medical Students, MBA Students. They all have a Name and Roll Number (Common traits).
#Without Inheritance: You would rewrite name and roll_number in every single class.
#With Inheritance: You write it once in a Student class and "inherit" it in others.
#  It follows the DRY (Don't Repeat Yourself) principle, which is the golden rule of clean coding.

#Socho hum aik E-commerce website bana rahe hain. Har cheez (Gadget) ka aik Brand aur Price hota hai.
#Lekin har gadget ke apne features hote hain (Smartphone ki Battery hoti hai, Laptop ki RAM hoti hai).

#Parent class (Generic)
class Device:
    def __init__(self, brand, price):
        self.brand =  brand
        self.price = price

    def get_details(self):
        return f"Brand: {self.brand}, Price: ${self.price}"
    

#Child class (Specialized)
class smart_phone(Device):
    def __init__(self, brand, price, battery_life):
        super().__init__(brand, price)   #super() se hum ne parent ka 'brand' aur 'price' wala kaam le liya
        self.battery_life = battery_life

    def get_batteryInfo(self):
        return f"Battery Life: {self.battery_life} hours"

