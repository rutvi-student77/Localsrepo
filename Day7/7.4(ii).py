"ii Write a program to dump/write data in json file."

import json

def write_to_json_file(output.json, data):
    try:
    
        with open(output.json, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Data has been written to {output.json}")
    except Exception as e:
        print(f"Error: {e}")


data = {
    "name": "Jane Doe",
    "age": 25,
    "city": "San Francisco",
    "isStudent": False
}

file_path = 'output.json' 
write_to_json_file(output.json, data)

