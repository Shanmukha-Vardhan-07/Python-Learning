class PaymentMethod:
    def __init__(self, account_holder):
        self.account_holder = account_holder

    def payment_info(self):
        print("Payment Account Holder:", self.account_holder)


class CreditCard(PaymentMethod):
    def __init__(self, account_holder, card_number):
        super().__init__(account_holder)
        self.card_number = card_number

    def make_payment(self):
        print("Payment made using Credit Card")
        print("Credit Card Number:", self.card_number)


class UPI(PaymentMethod):
    def __init__(self, account_holder, upi_id):
        super().__init__(account_holder)
        self.upi_id = upi_id

    def make_payment(self):
        print("Payment made using UPI")
        print("UPI ID:", self.upi_id)


class NetBanking(PaymentMethod):
    def __init__(self, account_holder, bank_name):
        super().__init__(account_holder)
        self.bank_name = bank_name

    def make_payment(self):
        print("Payment done using NetBanking")
        print("Bank Name:", self.bank_name)


while True:

    holder = input("\nEnter the account holder name: ")

    print("\nChoose Payment Method")
    print("1. Credit Card")
    print("2. UPI")
    print("3. Net Banking")
    print("4. Exit")

    choice = int(input("Enter the choice: "))

    if choice == 1:
        card_number = input("Enter card number: ")
        payment = CreditCard(holder, card_number)

    elif choice == 2:
        upi_id = input("Enter UPI ID: ")
        payment = UPI(holder, upi_id)

    elif choice == 3:
        bank_name = input("Enter bank name: ")
        payment = NetBanking(holder, bank_name)

    elif choice == 4:
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice")
        continue

    print("\n--- Payment Details ---")
    payment.payment_info()
    payment.make_payment()