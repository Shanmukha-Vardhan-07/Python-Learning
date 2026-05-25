num=int(input("Enter the number to check palindrome or not:"))

original=num
rev=0

while num > 0:
    digit=num % 10
    rev=rev*10+digit
    num=num//10

if original==rev:
    print(original,"is a Palindrome Number")
else:
    print(original,"is Not a Palindrome Number")        