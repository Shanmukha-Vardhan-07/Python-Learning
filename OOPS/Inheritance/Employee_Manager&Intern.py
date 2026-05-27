class Employee:
    def __init__(self,name):
        self.name=name

    def salary_information(self):
        print("Employee salary Information")

class Manager(Employee):
    def salary_information(self):
        print(self.name,"is a manager")
        print("Salary is : 80000")

class Intern(Employee):
    def salary_information(self):
        print(self.name,"is a Intern")
        print("Salary is : 15000")

name=input("Enter the name of Employee:")

print("\n1. Manager")
print("2. Intern")

choice = int(input("Enter your choice: "))

if choice == 1:

    employee = Manager(name)
    employee.salary_information()

elif choice == 2:

    employee = Intern(name)
    employee.salary_information()

else:
    print("Invalid Choice")
