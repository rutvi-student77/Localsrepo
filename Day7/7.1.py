"i) Create a Program that takes a string (a random name). If the last character of the name is an  a return True, otherwise return False."
def check_last_character(name):
    if name[-1].lower() == 'a':  
        return True
    else:
        return False

name_1 = "Mariae"
name_2 = "Johna"

print(check_last_character(name_1))
print(check_last_character(name_2)) 
