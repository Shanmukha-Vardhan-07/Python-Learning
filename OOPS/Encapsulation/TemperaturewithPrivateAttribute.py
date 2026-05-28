class Temperature:
    def __init__(self,celsius):
        self._celsius=celsius

    def get_celsius(self):
        return self._celsius
    
    def set_celsius(self,celsius):
        self._celsius= celsius

    def get_fahrenheit(self):
        return (self._celsius * 9/5)+32
    
temp_value=float(input("Enter the celsius Value:"))

temp=Temperature(temp_value)

print("\nTemperature in Celsius:", temp.get_celsius())
print("Temperature in Fahrenheit:", temp.get_fahrenheit())

new_temp = float(input("\nEnter new Celsius temperature: "))
temp.set_celsius(new_temp)

print("\nUpdated Temperature in Celsius:", temp.get_celsius())
print("Updated Temperature in Fahrenheit:", temp.get_fahrenheit())