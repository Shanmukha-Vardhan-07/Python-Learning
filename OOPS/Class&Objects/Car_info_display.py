class Car:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year

    def display_info(self):
        print("---Car Information---")
        print("Car Brand:",self.brand)
        print("Car Model:",self.model)
        print("Year:",self.year)

brand=input("Enter the brand name:")
model=input("Enter the car model:")
year=int(input("Enter the car publish year:"))

car1=Car(brand,model,year)

car1.display_info()