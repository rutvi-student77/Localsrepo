"Create a function/input that counts the integer's number of digits.Solve this without using strings."

def count(number):
    number = abs(number)
    
    if number == 0:
        return 1
    
    digit_count = 0
    
    while number > 0:
        number //= 10  
        digit_count += 1 
    
    return digit_count

print(count(318))      
print(count(-925638))   
print(count(4666))     
print(count(-314890))  
print(count(654321))   
print(count(638476))  
