#----Mastering Custom Exceptions (Error Handling)----#
"""What----
Humne try-except toh dekha hai, lekin "Pro" developers sirf Python ke built-in errors (jaise ValueError) 
par rely nahi karte. Wo apne errors banate hain jinhain Custom Exceptions kehte hain.

WHY-----
Socho tum E-commerce app bana rahi ho. Agar koi user discount 100% se zyada daal de, toh ValueError toh nahi aayega, 
lekin business logic ghalat ho jayegi. Yahan tum apna error "generate" (raise) karti ho."""




# Custom exception class for invalid discount values
class InvalidDiscountError(Exception):
    pass  

def apply_discount(price, discount):
    #checking if the discount is in valid range
    if discount > 100:
        # Raise the custom error if discount exceeds 100%
        raise InvalidDiscountError(" Discount can't be more then 100%! ")
    # calculate the final price
    final_price = price - (price * discount/100 )
    return final_price




"""why write "pass"???
 pass is a placeholder, Python is very strict about indentation and structure. Whenever you write a 
class definition or a def function, Python expects an indented block of code to follow the colon (:).

 If you leave the body of the class empty, Python will throw an IndentationError 
because it thinks you forgot to write the code inside the class."""