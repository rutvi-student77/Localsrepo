"Given an integer, create a function that returns the next prime. If the number is prime, return the number itself."

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def next_prime(n):
    if is_prime(n):
        return n
    else:
        n += 1
        while not is_prime(n):
            n += 1
        return n

# Test cases
print(next_prime(5))  # ➞ 5 (since 5 is prime)
print(next_prime(6))  # ➞ 7 (next prime after 6 is 7)
print(next_prime(10))  # ➞ 11 (next prime after 10 is 11)
print(next_prime(13))  # ➞ 13 (since 13 is prime)
