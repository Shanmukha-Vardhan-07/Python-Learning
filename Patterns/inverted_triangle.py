n=int(input("Enter the number of rows:"))

for i in range(n):
    for j in range(i,n):
        print("*",end=' ')
    print()    