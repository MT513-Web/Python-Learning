#------OS Module aur File Checking.-----

import os

def check_or_creat_file(fileName):
    if os.path.exists(fileName):
        return f"File '{fileName}' is found."
    
    else:
        with open(fileName, "w") as f:
            f.write("---My NOTES--- \n")
        return f"File '{fileName}' was not found, So I make it!"
    
def add_note(fileName, note):
    with open(fileName, "a") as f:
        f.write(note + "\n")
    return "Note saved..."
