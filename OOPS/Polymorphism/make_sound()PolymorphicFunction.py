class Dog:
    def speak(self):
        print("Dog Says :Wood Woof")

class Cat:
    def speak(self):
        print("Cat says : Meow Meow")

class Duck:
    def speak(self):
        print("Duck Says: Quack Quack")

def make_sound(animal):
    animal.speak()

dog=Dog()
cat=Cat()
duck=Duck()

make_sound(dog)
make_sound(cat)
make_sound(duck)
