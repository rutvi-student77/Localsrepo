"Import python program(previous OOP based calculator) and run in this program."

import json

class Calculator:
    def __init__(self):
        pass
    
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero."
    
    def power(self, a, b):
        return a ** b

def write_to_json_file(file_path, data):
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Results have been written to {file_path}")
    except Exception as e:
        print(f"Error: {e}")

def read_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            print(json.dumps(data, indent=4))  
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from the file.")

if __name__ == "__main__":
    calc = Calculator()
    
    addition_result = calc.add(10, 5)
    subtraction_result = calc.subtract(10, 5)
    multiplication_result = calc.multiply(10, 5)
    division_result = calc.divide(10, 5)
    power_result = calc.power(2, 3)
    
    results = {
        "addition": addition_result,
        "subtraction": subtraction_result,
        "multiplication": multiplication_result,
        "division": division_result,
        "power": power_result
    }
    
    file_path = 'calculator_results.json'
    
    write_to_json_file(file_path, results)
    
    read_json_file(file_path)
