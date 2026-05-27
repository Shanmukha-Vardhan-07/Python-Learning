class Vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def display(self):
        print("---Vehicle Details---")
        print("Brand:",self.brand)
        print("Model:",self.model)

    def Fuel_type(self):
        print("Fuel Type: Petrol/Diesel")

class ElectricVehicle(Vehicle):
    def __init__(self,brand,model,battery_capacity):
        super().__init__(brand,model)
        self.battery_capacity=battery_capacity

    def Fuel_type(self):
        print("Fuel Type:Electric")

    def battery_info(self):
        print("Battery capacity:",self.battery_capacity,"Kwh")


brand=input("Enter the Brand:")
model=input("Enter the model:")
battery=int(input("Enter the Battery Capacity:"))

ev=ElectricVehicle(brand,model,battery)

print("Vehicle Details:")
ev.display()

ev.Fuel_type()

ev.battery_info()