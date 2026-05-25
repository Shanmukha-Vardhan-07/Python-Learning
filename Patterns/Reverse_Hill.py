n=int(input("Enter number of rows:"))

for i in range(n):
    for j in range(i):
        print(' ',end=' ')
    for j in range(i,n-1):
        print('*',end=' ')
    for j in range(i,n):
        print('*',end=' ')
    print()            