"Create a Circle constructor that creates a circle with a radius provided by an argument. The circles constructed must have two getters getArea() (PI*r^2) and getPerimeter() (2*PI*r) which give both respective areas and perimeter (circumference)."
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def getArea(self):
        return math.pi * self.radius ** 2
    
    def getPerimeter(self):
        return 2 * math.pi * self.radius

circy = Circle(11)
print(circy.getArea())  

circy = Circle(4.44)
print(circy.getPerimeter())  

