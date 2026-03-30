#_...about_Strings..._ String Manipulation
# String Indexing, Slicing, and Built-in Methods.
#_Uses_in_real_life_
#1.Social Media Apps (Instagram/Facebook/X),2.E-commerce (Amazon/Daraz),3.Security&Login System,4.Microsoft Word&Google Docs,5. Data Science & AI

#1. String Indexing
Name = "Ayesha"
print(Name[0])
print(Name[-1])

#2. String Slicing
variable = "Good Luck"
print(variable[0:7])
print(variable[-1:5])#Learning reverse slicing
print(variable[::5])#reverse_method
print(variable[::-1])#reverse_method

#_Todays_challenge_
name = "Rubina Afzal"
print(name.upper())
print(name.lower())
print(len(name))
print(name.strip())#remove_extra_space
print(name.replace("Rubina", "Ayesha"))
print(name[::11])
print(name[0], name[-1])#1st_last_letter
print(name[::-1])

#extra_"Searching & Counting"
paragraph = input("Write your paragraph:")
word = input("Write your required word:")
if word in paragraph:
    print("Yes, it is present.")
else:
    print("No, it is not present.")
print(paragraph.replace("girl", "boy"))
print(paragraph.count(word))
total = paragraph.count(word)
print(f"The word '{word}' appears '{total}' times.")


