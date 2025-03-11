"Create a function/input that, given a number, returns the corresponding value of that index in the Fibonacci series.,The Fibonacci Sequence is the series of numbers:,1, 1, 2, 3, 5, 8, 13, 21, 34, ...,	fibonacci(3) ➞ 3,fibonacci(7) ➞ 21,fibonacci(12) ➞ 233"

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    
    a, b = 1, 1
    
    for _ in range(3, n + 1):
        a, b = b, a + b  
    
    return b

print(fibonacci(3))   
print(fibonacci(7))   
print(fibonacci(12))  
