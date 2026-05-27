class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)
        print("Current Balance:", self.balance)

    def withdraw(self, amount):

        if amount > self.balance:
            raise ValueError("Insufficient Balance! Overdraft not allowed.")

        self.balance -= amount
        print("Withdrawn:", amount)
        print("Current Balance:", self.balance)



initial_balance = float(input("Enter initial balance: "))

account = BankAccount(initial_balance)

while True:

    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        amount = float(input("Enter deposit amount: "))
        account.deposit(amount)

    elif choice == 2:

        amount = float(input("Enter withdraw amount: "))

        try:
            account.withdraw(amount)

        except ValueError as e:
            print(e)

    elif choice == 3:

        print("Thank You!")
        break

    else:
        print("Invalid Choice")