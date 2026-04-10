#*args (Arguments)
def sum_all(*numbers):
    total = 0
    for n in numbers:
        total += n
    return total
print(sum_all(15, 15))
print(sum_all(1,4,2,3,5,6))
print("-" *20)
       

#----------------------------Task---------------------------------#
def show_movies(*movies):
    for m in movies:
        print(f"I want to wathc: {m}")
show_movies("The Lion king", "Inception")
print("-" *20)
show_movies("Batman", "Spiderman", "Ironman", "You", "Frozan") 



#----------------------------Task1-----------------------------------#
def movie_counter(*movies):
    total = len(movies)
    print(f"Total Movies in Watchlist are: {total}")
    for m in movies:
      print(f"- {m}")
movie_counter("Frozan", "Inception", "You")


#-------------Easy Practice Task — The Party Guest List--------------#
def welcome_guest(*names):
   total = len(names)
   print(f"Total guests are {total}.")
   print("-.-.-." *5)
   print(f"~.~.~.Welcome to the party .~.~.~")
   print("-.-.-." *5)
   for n in names:
      print(f"- {n}")
welcome_guest("Ayesha", "Hina")



#---------------------The "Favorite Foods" Shoutout--------------------#
def food_shoutout(*foods):
    print("~.----My Fav Foods----.~")
    for f in foods:
      print(f" - I love {f.upper()}!")
food_shoutout("Biryanii", "Macaroni", "Ice-Cream")



#---------------------Taking Input from user--------------------#
user_food = []
while True:
   input_ = input("Which is your Fav food ? (or type 'done' to finish)").strip().lower()
   
   if input_ == 'done' :
      break
   
   user_food.append(input_)
   print(f"Added: {input_}")
print("Your Fav Foods are: ", *user_food)

