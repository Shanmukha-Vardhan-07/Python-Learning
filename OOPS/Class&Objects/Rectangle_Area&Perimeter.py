class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2*(self.length+self.width)

    def is_square(self):
        if self.length==self.width:
            return True
        else:
            return False

length=float(input("Enter the length:"))
width=float(input("Enter the width:"))

rect=Rectangle(length,width)

print("Area:",rect.area())
print("Perimeter:",rect.perimeter())

if rect.is_square():
    print("It is a square")
else:
    print("It is not a square")    