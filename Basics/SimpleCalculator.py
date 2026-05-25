a=int(input("Enter the a value:"))
b=int(input("Enter the b value:"))

print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

choice=int(input("Enter the choice:"))

if choice==1:
    print("Result:",a+b)
elif choice==2:
     print("Result:",a-b)
elif choice==3:
      print("Result:",a*b)
elif choice==4:
      print("Result:",a/b)
else:
     print("Invalid Choice")               
