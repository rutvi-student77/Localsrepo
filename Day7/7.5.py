"Import python program(previous OOP based calculator) and run in this program."
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def sum_of_primes(numbers):
    total_sum = 0
    for num in numbers:
        if is_prime(num):
            total_sum += num
    return total_sum

class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, x, y):
        self.result = x + y
        return self.result

    def subtract(self, x, y):
        self.result = x - y
        return self.result

    def multiply(self, x, y):
        self.result = x * y
        return self.result

    def divide(self, x, y):
        if y != 0:
            self.result = x / y
        else:
            self.result = "Error! Division by zero."
        return self.result

    def get_result(self):
        return self.result

def main():
    numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
    prime_sum_result = sum_of_primes(numbers)
    print(f"The sum of all prime numbers in the list is: {prime_sum_result}")

    calc = Calculator()
    print("\nBasic Calculator")
    while True:
        print("\nOptions:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        choice = input("Enter choice: ")

        if choice == '5':
            print("Exiting calculator.")
            break
        elif choice in ['1', '2', '3', '4']:
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))

            if choice == '1':
                print(f"{x} + {y} = {calc.add(x, y)}")
            elif choice == '2':
                print(f"{x} - {y} = {calc.subtract(x, y)}")
            elif choice == '3':
                print(f"{x} * {y} = {calc.multiply(x, y)}")
            elif choice == '4':
                print(f"{x} / {y} = {calc.divide(x, y)}")
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()
