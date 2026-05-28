class CreditCard:
    def __init__(self,creditcard,cvv):
        self._creditcard=creditcard
        self._cvv=cvv

    def masked_number(self):
        last_four=self._creditcard[-4:]
        return "*"*(len(self._creditcard)-4)+last_four
    
card_number = input("Enter card number: ")
cvv = input("Enter CVV: ")

card = CreditCard(card_number, cvv)

print("\nMasked Card Number:", card.masked_number())