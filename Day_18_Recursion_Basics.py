#Recursion (Functions calling themselves)
def countdown(n):
    if n == 0:
        print("Blast Off!")
    else:
        print(n)
        countdown(n - 1)
countdown(5)

#-----The Factorial------#
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))


#-----The Power of Number------#
def power(base, exp):
    if exp == 0:
        return 1
    else:
        return base * power(base, exp - 1)
print(power(2, 3))



#------String Reverse------#
def reverse_str(s):
    if len(s) <= 1:
        return s
    
    return s[-1] + reverse_str(s[:-1])
print(reverse_str("Ayesha"))



