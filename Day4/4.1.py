"Create a function that returns the amount of duplicate characters in a string. It will be case sensitive and spaces are included. If there are no duplicates, return 0."

def count_duplicates(input_string):
    char_count = {}
    
    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    duplicate_count = sum(1 for count in char_count.values() if count > 1)
    
    return duplicate_count

input_string = "aabcad "
result = count_duplicates(input_string)
print(result)  
