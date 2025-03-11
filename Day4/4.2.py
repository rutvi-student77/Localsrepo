"Create a function/input that counts the integer's number of digits.Solve this without using strings."

def count_digits(number):
    if number == 0:
        return 1
    
    number = abs(number)
    
    digit_count = 0
    
    while number > 0:
        number //= 10  
        digit_count += 1  
    
    return digit_count

number = 123456789
result = count_digits(number)
print(result)  
