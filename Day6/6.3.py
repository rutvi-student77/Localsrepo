
class Employee:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.fullname = f"{first_name} {last_name}"  
        self.email = f"{first_name.lower()}.{last_name.lower()}@company.com"  

emp_1 = Employee("John", "Smith")
emp_2 = Employee("Mary", "Sue")
emp_3 = Employee("Antony", "Walker")

print(emp_1.fullname) 
print(emp_2.email)    
print(emp_3.first_name) 