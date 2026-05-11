#-----JSON (JavaScript Object Notation)-----#

#1. Why use the json module?
#Python has a built-in library called json. We import it because it handles all the "brackets and quotes" headache for us.
#It converts Python Dictionaries into text files automatically.

#2. Saving Data (dump)
#We use json.dump(). It takes your Python Dictionary and turns it into a JSON text file.

#3. Loading Data (load)
#We use json.load(). It reads the text file and converts it back into a Python Dictionary so your program can read it.

import json
# from textwrap import indent

def save_data(filename, data):
    #overwriting file with new data
    with open(filename, "w") as f:
        json.dump(data, f, indent=4) #indent=4 make it pretty
    return "Data saved as JSON!"

def load_data(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f) # Converts JSON text back to Python Dictionary
    except FileNotFoundError:
        return {} # If no file, return an empty dict