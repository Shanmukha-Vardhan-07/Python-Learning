import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


def print_areas(shapes):
    for shape in shapes:
        print("Area =", shape.area())


circle = Circle(7)
rectangle = Rectangle(10, 5)
triangle = Triangle(6, 4)


shapes = [circle, rectangle, triangle]

print_areas(shapes)
