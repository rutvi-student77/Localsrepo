"ii Write a program to dump/write data in json file."

import json





data_to_write = {
    "name": "Jane ",
    "age": 25,
    "email": "janedoe@example.com",
    "is_admin": False
}

file_path =open( 'student.json',"w") 
json.dump(data_to_write, file_path, indent=4)


