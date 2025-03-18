"ii) Create a Program that takes a string (a random name). If the last and first character of the name is an d, return True, otherwise return False."

def check_first_and_last(name):
    # Check if both the first and last characters of the name are 'd'
    if name[0].lower() == 'd' and name[-1].lower() == 'd':
        return True
    else:
        return False

# Example usage
name_1 = "david"
name_2 = "dannyd"
name_3 = "john"

print(check_first_and_last(name_1))  # Output: True
print(check_first_and_last(name_2))  # Output: True
print(check_first_and_last(name_3))  # Output: False
