"Create a program that takes three arguments a, b, c and returns the sum of the numbers that are evenly divided by c from the range a, b inclusive"
def sum_of_divisible(a, b, c):
    
    total_sum = 0
    
    for num in range(a, b + 1):
        if num % c == 0:
            total_sum += num
    
    return total_sum

# Example usage
a = int(input("Enter the starting number (a): "))
b = int(input("Enter the ending number (b): "))
c = int(input("Enter the divisor (c): "))

result = sum_of_divisible(a, b, c)
print(f"The sum of numbers between {a} and {b} that are divisible by {c} is: {result}")
