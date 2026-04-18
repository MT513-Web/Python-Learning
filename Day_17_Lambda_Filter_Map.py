#Lambda Functions or "Anonymous Functions"
# Syntax: lambda arguments : expression
#filter():Strainer ki tarah kaam karta hai (Sirf wohi rakhta hai jo condition pass kare).
#map():Transformer ki tarah kaam karta hai (List ki har item par aik hi operation apply kar deta hai)


double_lambda = lambda n : n * 2
print(double_lambda(5))

#------Day 17 Tasks: The Shortcut Math------#
#Add
add_lambda = lambda a, b : a + b
print(add_lambda(4, 5))

#Square
power_lambda = lambda n : n*n
print(power_lambda(3))

#Length
length = lambda s : len(s)
print(length("Ayesha"))
print(length("python"))

#.-----Level Up (Lambda with Filter)-----.
#with_list
nums = [5, 6, 17, 13, 12, 24, 23]

greater_num = list(filter(lambda x : x > 20, nums))
print(greater_num) 


# .----Final Mastery — The map() Function-----.
prices = [500,600, 700, 900, 1500]
discount = list(map(lambda p: p - 50, prices))
print(discount)


square_list = [2, 4, 7, 10, 3]
square = list(map(lambda x : x * x, square_list))
print(square)
