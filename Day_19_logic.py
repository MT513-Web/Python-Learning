#making File (my_logic.py)
def Welcome(name):
    return f"Asslamo-o-Alaikum {name}!"

def power(n):
    return n*n

#---_The Guessing Game_---
def check_guess(user_num, secret_num):
     if user_num == secret_num:
          return "Great...You win boss."
     else:
          return f"Oopss...Try again champ.Secret was {secret_num}"