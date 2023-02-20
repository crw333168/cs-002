"""
Christina Wang	8/17/22	CSCI-UA 2 - 006
Assignment #8 Problem #1
"""

import math

#class
class Circle:
    def __init__(self, radius, x, y):
        self.radius = radius
        self.x = x
        self.y = y

    def get_area(self):
        area= math.pi*float((self.radius)**2)
        print(format( area, ".2f" ))

    def get_circumference(self):
        circ= 2*math.pi*float(self.radius)
        print(format( circ, ".2f" ))

#two circles
a=Circle(6,5,3)

b=Circle(3,15,7)

#get info
print("Circle #1")
print("* Coordinates: (",a.x, ", ", a.y,")")
print("* Area: ", end="")
a.get_area()
print("* Perimeter: ", end="")
a.get_circumference()

print("Circle #2")
print("* Coordinates: (",b.x, ", ", b.y,")")
print("* Area: ", end="")
b.get_area()
print("* Perimeter: ", end="")
b.get_circumference()
