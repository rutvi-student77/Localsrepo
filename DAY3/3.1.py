"Write a Program that takes coordinates of two points on a two-dimensional plane and returns the length of the line segment connecting those two points."
import math

def calculate_distance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

distance = calculate_distance(x1, y1, x2, y2)

print(f"The length of the line segment connecting the points ({x1}, {y1}) and ({x2}, {y2}) is: {distance}")
