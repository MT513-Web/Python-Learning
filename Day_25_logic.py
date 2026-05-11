#------The "Filter" Technique--------

def del_note(filename, note_to_del):
    with open(filename, "r") as f:
        lines = f.readlines()

    with open(filename, "w") as f:
        for line in lines:
            if line.strip() != note_to_del:
                f.write(line)

    return f"'{note_to_del}' is deleted, if it was present in lines! \n"

