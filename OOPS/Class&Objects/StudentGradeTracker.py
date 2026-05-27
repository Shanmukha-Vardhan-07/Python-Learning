class Student:
    def __init__(self,name):
        self.name=name
        self.grades=[]

    def add_grade(self,grade):
        self.grades.append(grade)
        print("Grade Added successfully")

    def average(self):
        if len(self.grades)==0:
            return 0

        return sum(self.grades)/len(self.grades)

    def highest(self):
        if len(self.grades)==0:
            return 0

        return max(self.grades)

name=input("Enter the name of student:")

student=Student(name)

n=int(input("Enter the number of grades:"))

for i in range(n):
    grade=float(input(f"Enter the grade of {i+1}:"))
    student.add_grade(grade)

print("\nStudent Name:", student.name)
print("Grades:", student.grades)
print("Average Grade:", student.average())
print("Highest Grade:", student.highest())  