"i) Write a program to read json file and show in terminal."
import json

def read_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            print(json.dumps(data, indent=4))  
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from the file.")

file_path = 'D:\gitdemos\Localsrepo\Day7\example.json' 
read_json_file(file_path)
