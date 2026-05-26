class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully")
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully")
        else:
            print("Insufficient balance")

    def check_balance(self):
        print(f"Available Balance: ₹{self.balance}")

class SavingAccount(BankAccount):
    def __init__(self,account_holder,balance=0,interest_rate=5):
        super().__init__(account_holder,balance)
        self.interest_rate=interest_rate

    def add_interest(self):
        interest=(self.balance*self.interest_rate)/100
        self.balance+=interest
        print(f"Interest of ₹{interest} added successfully")

class CheckingAccount(BankAccount):
    def __init__(self,account_holder,balance=0,overdraft_limit=1000):
        super().__init__(account_holder,balance)
        self.overdraft_limit=overdraft_limit

    def withdraw(self, amount):
        if amount<=(self.balance+self.overdraft_limit):
            self.balance-=amount
            print(f"{amount} withdrawn successfully")
        else:
            print("Overdraft limit exceeded")

name = input("Enter Account Holder Name: ")
balance = float(input("Enter Initial Balance: "))

print("\nChoose Account Type")
print("1. Savings Account")
print("2. Checking Account")

account_type = int(input("Enter your choice: "))

if account_type == 1:
    interest_rate = float(input("Enter Interest Rate: "))
    account = SavingAccount(name, balance, interest_rate)

elif account_type == 2:
    overdraft_limit = float(input("Enter Overdraft Limit: "))
    account = CheckingAccount(name, balance, overdraft_limit)

else:
    print("Invalid Account Type")
    exit()



while True:
    print("\n------ BANK MENU ------")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")

    if isinstance(account, SavingAccount):
        print("4. Add Interest")
        print("5. Exit")
    else:
        print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = float(input("Enter amount to deposit: "))
        account.deposit(amount)

    elif choice == 2:
        amount = float(input("Enter amount to withdraw: "))
        account.withdraw(amount)

    elif choice == 3:
        account.check_balance()

    elif choice == 4 and isinstance(account, SavingAccount):
        account.add_interest()

    elif (choice == 5 and isinstance(account, SavingAccount)) or \
         (choice == 4 and isinstance(account, CheckingAccount)):
        print("Thank You for using the Bank System")
        break

    else:
        print("Invalid Choice")                
       



                


             