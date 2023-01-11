# Exercise 1 : Built-In Functions

print("abs(-5) = ", abs(-5))

print("int(3.14) = ", int(3.14))

name = input("What is your name? ")
print("Hello, ", name)

"""
This program demonstrates the use of three built-in Python functions: abs(), int(), and input().
The function abs() returns the absolute value of a number. The function int() converts a value to an integer.
The function input() reads a line from input and returns it as a string.
"""


# Daily Challenge - Circle
import math

class Circle():
    def __init__(self, radius=None, diameter=None):
        if radius:
            self.radius = radius
            self.diameter = radius * 2
        elif diameter:
            self.radius = diameter / 2
            self.diameter = diameter
        else:
            raise ValueError("Circle must be defined by either radius or diameter.")
    
    def __str__(self):
        return f'Circle with radius: {self.radius}'
    
    def __repr__(self):
        return f'Circle({self.radius})'
    
    def __add__(self, other):
        return Circle(radius=self.radius + other.radius)
    
    def __lt__(self, other):
        return self.radius < other.radius
    
    def __eq__(self, other):
        return self.radius == other.radius

    def area(self):
        return math.pi * (self.radius ** 2)

c1 = Circle(radius=2)
c2 = Circle(diameter=4)
c3 = Circle(radius=3)
c4 = Circle(radius=5)
print(c1)
print(c2)
print(c1.area())
print(c2.area())
c5 = c1 + c2
print(c5)
print(c1 < c2)
print(c1 == c2)
circles = [c1, c2, c3, c4]
print
