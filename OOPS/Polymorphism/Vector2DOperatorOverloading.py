class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"


x1 = int(input("Enter x value of Vector 1: "))
y1 = int(input("Enter y value of Vector 1: "))

x2 = int(input("Enter x value of Vector 2: "))
y2 = int(input("Enter y value of Vector 2: "))

v1 = Vector2D(x1, y1)
v2 = Vector2D(x2, y2)

result = v1 + v2

print("\nVector 1:", v1)
print("Vector 2:", v2)
print("Resultant Vector:", result)