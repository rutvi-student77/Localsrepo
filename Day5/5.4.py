
def to_dict(char_list):
    return [{char: ord(char)} for char in char_list]

# Test cases
print(to_dict(["a", "b", "c"]))  
print(to_dict(["^"]))  
print(to_dict([])) 
