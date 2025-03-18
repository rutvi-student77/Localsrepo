"Create a function that takes a dictionary of student names and returns a list of student names in alphabetical order."

def sort_students(student_dict):
    return sorted(student_dict.keys())

students = {
    "John": 85,
    "Alice": 92,
    "Bob": 78,
    "Charlie": 88
}
print(sort_students(students))  
