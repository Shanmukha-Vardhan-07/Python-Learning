class BankAccount:
    def __init__(self,account_holder,balance=0):
        self.account_holder=account_holder
        self.balance=balance

    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(f"{amount} is deposited succesfully")
        else:
            print("Invaild amount")

    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            print(f"{amount} is withdraw successfully")
        else:
            print("No sufficient amount")

    def view_balance(self):
        print("Available balance:",self.balance)


name=input("Enter the name of account holder:")
balance=float(input("Enter the balance:"))    

account1=BankAccount(name,balance)

while True:
    print("----Bank Menu----")
    print("1.Deposit")
    print("2.Withdraw")
    print("3.Check Balance")
    print("4.Exit")

    choice=int(input("Enter your choice:"))

    if choice == 1:
        amount=float(input("Enter the amount to Deposit:"))
        account1.deposit(amount)
    elif choice==2:
        amount=float(input("Enter the amount to Deposit:"))
        account1.withdraw(amount)
    elif choice==3:
        account1.view_balance()
    elif choice==4:
        print("Thank You")
        break        
    else:
        print("Invalid Choice")    
        