def is_valid_pin(pin):
    if (len(pin) == 4 or len(pin) == 6) and pin.isdigit() and not any(char.isspace() for char in pin):
        return True
    return False


pin_input = input("Enter a PIN: ")

if is_valid_pin(pin_input):
    print(f"{pin_input} is a valid PIN.")
else:
    print(f"{pin_input} is not a valid PIN.")
