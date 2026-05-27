import math
class Shape:
    def area(self):
        pass
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return math.pi*self.radius*self.radius

    def perimeter(self):
        return 2*math.pi*self.radius

class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        return self.length*self.width

    def perimeter(self):
        return 2*(self.length+self.width)

class Triangle(Shape):
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c

    def perimeter(self):
        return self.a+self.b+self.c

    def area(self):
        s=self.perimeter()/2
        return math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))

while True:
    print("Choose Shape:")
    print("1.Circle")
    print("2.Rectangle")
    print("3.Triangle")
    print("4.Exit")

    choice=int(input("Enter the choice:"))

    if choice==1:
        radius=float(input("Enter the radius:"))
        c=Circle(radius)

        print("Area =",c.area())
        print("Perimeter=",c.perimeter())
    elif choice==2:
        length=float(input("Enter the length:"))
        width=float(input("Enter the width:"))

        r=Rectangle(length,width)

        print("Area=",r.area())
        print("Perimeter=",r.perimeter())

    elif choice==3:
        a=float(input("Enter the a value:"))           
        b=float(input("Enter the b value:"))           
        c=float(input("Enter the c value:"))

        t=Triangle(a,b,c)

        print("Area=",t.area())
        print("Perimeter=",t.perimeter())

    elif choice==4:
        print("Exiting")
        break
    else:
        print("Invalid choice")               

