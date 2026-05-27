class Animal:
    def speak(self):
        print("Animal makes sound")

class Dog(Animal):
    def speak(self):
        print("Dog says:Bark")

class Cat(Animal):
    def speak(self):
        print("Cat says : Meow")

dog=Dog()
cat=Cat()

dog.speak()
cat.speak()
