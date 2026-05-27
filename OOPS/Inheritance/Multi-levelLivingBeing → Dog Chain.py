class LivingBeing:
    def __init__(self,name):
        self.name=name

    def breathe(self):
        print(self.name,"Is Breathing")

class Animal(LivingBeing):
    def __init__(self,name,habitat):
        super().__init__(name)
        self.habitat=habitat

    def eat(self):
        print(self.name,"Eats Food")

class Mammal(Animal):
    def __init__(self,name,habitat,fur_color):
        super().__init__(name,habitat)
        self.fur_color=fur_color

    def walk(self):
        print(self.name,"Is walking")

class Dog(Mammal):
    def __init__(self,name,habitat,fur_color,breed):
        super().__init__(name,habitat,fur_color)
        self.breed=breed

    def bark(self):
        print(self.name,"Is Barking")

name = input("Enter dog name: ")
habitat = input("Enter habitat: ")
fur_color = input("Enter fur color: ")
breed = input("Enter breed: ")

dog1 = Dog(name, habitat, fur_color, breed)

print("\n--- Dog Details ---")
print("Name:", dog1.name)
print("Habitat:", dog1.habitat)
print("Fur Color:", dog1.fur_color)
print("Breed:", dog1.breed)

print("\n--- Methods Output ---")
dog1.breathe()
dog1.eat()
dog1.walk()
dog1.bark()                         