
from Day_33_logic import smart_phone



#creaying specific smartphone object
my_phone = smart_phone("Infinix", 35000, 24)

#inherited methods work
print(my_phone.get_details())

#child's own method work
print(my_phone.get_batteryInfo())

