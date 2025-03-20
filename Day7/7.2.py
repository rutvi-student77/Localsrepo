import json
dictionary = {
    "data": [
        {"Name": "rutvi", "age": 28, "email": "xyz@gmail.com"}],
    "Marks": [
        {"English": 100, "Gujrati": 98}],
    "count": [5, 8, 9, 10,{"name":[1,2,3]}]
}
json_object = json.dumps(dictionary, indent=4)
print(json_object)

marks = dictionary["Marks"][0]["Gujrati"]
print("Gujarati Marks:")
print(marks)

count = [i for i in dictionary["count"] if i == 9]
print("Count equal to 9:")
print(count)

count= dictionary["count"][4]["name"][1]
print(count)

