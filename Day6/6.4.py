class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

def people_sort(people, attribute):
    return sorted(people, key=lambda person: getattr(person, attribute))

p1 = Person("Michael", "Smith", 40)
p2 = Person("Alice", "Waters", 21)
p3 = Person("Zoey", "Jones", 29)
print([person.firstname for person in people_sort([p1, p2, p3], "firstname")])
print([person.lastname for person in people_sort([p1, p2, p3], "lastname")])
print([person.age for person in people_sort([p1, p2, p3], "age")])

