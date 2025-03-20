"i) Write a program to read json file and show in terminal."

import json

f = open('data.json',)

data = json.load(f)

for i in data['stud_info']:
    print(i)

f.close()