"Create a function that takes an angle in radians and returns the corresponding angle in degrees rounded to one decimal place."
import math

def radians_to_degrees(radians):
    degrees = radians * (180 / math.pi)
    return round(degrees, 1)


print(radians_to_degrees(1))
print(radians_to_degrees(0))  
print(radians_to_degrees(math.pi))  
print(radians_to_degrees(math.pi / 2))  
