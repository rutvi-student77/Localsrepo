"Create a function that takes two numbers and a mathematical operator + - / * and will perform a calculation with the given numbers."

def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:  
            return num1 / num2
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Error: Invalid operator."

# Test cases
print(calculate(5, 3, '+'))  
print(calculate(5, 3, '-'))  
print(calculate(5, 3, '*'))  
print(calculate(5, 3, '/'))  
print(calculate(5, 0, '/'))  
print(calculate(5, 3, '%'))  
