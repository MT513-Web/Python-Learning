#----csv files Read, Write and Search----#
import csv
import os


#making headers
def setup_library(filename):

    # Agar file pehle se nahi hai, toh hi headers banayein
    if not os.path.exists(filename):
      with open(filename, mode = "w", newline="") as f:
        writer = csv.writer
        writer.writerow(["Book_Title", "Author", "Price", "Status"])

      return "New Library File Created!"
    return "File already exists."


#adding record
def add_book(filename, title, author, status, price):
    with open(filename, mode = "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([title, author, status, price])
        return "Book Added Successfully!"

#view record
def get_all_books(filename):
   records = []
   with open(filename, mode="r") as f:
      reader = csv.reader(f)
      for row in reader:
         records.append(row)
   return records

#search something in record
def search_book(filename, book_title):
  with open(filename, mode="r") as f:
      reader = csv.reader(f)
      for row in reader:
          if row[0].strip().lower() == book_title.strip().lower():
              return row
          
  return None

#DEl_books from Lib
def del_book(filename, book_title):
   all_books = []
   found = False

   with open(filename, mode="r") as f:
      reader = csv.reader(f)
      for row in reader:
         if row[0].strip().lower() != book_title.strip().lower():
          all_books.append(row)
         else:
          found = True 

   if found:
      with open(filename, mode="w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(all_books)
      return f"'{book_title}' has been deleted!"
   
   return f"'{book_title}' not found!"





