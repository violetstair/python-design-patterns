# 프록시 패턴 사용 사례
# 
from abc import ABCMeta, abstractmethod

class Payment(metaclass=ABCMeta):

    @abstractmethod
    def do_pay(self):
        pass


class Bank(Payment):

    def __init__(self):
        self.card = None
        self.account = None

    def __get_account(self):
        self.account = self.card # 카드 번호와 계좌 번호는 같다고 가정
        return self.account

    def __hash_funds(self):
        print("Bank :: checking if Account ", self.__get_account(), " has enough funds")

    def set_card(self, card):
        self.card = card

    def do_pay(self):
        if self.__hash_funds():
            print("Bank :: Paying the merchant")
            return True
        else:
            print("Bank :: Sorry, not enough funds")
            return False


class DebitCard(Payment):

    def __init__(self):
        self.bank = Bank()

    def do_pay(self):
        card = input("Proxy :: Punch in Card Number :  ")
        self.bank.set_card(card)
        return self.bank.do_pay()


class You:

    def __init__(self):
        print("YOU :: Let's buy the Denim shirt")
        self.debit_card = DebitCard()
        self.is_purchased = None

    def make_payment(self):
        self.is_purchased = self.debit_card.do_pay()

    def __del__(self):
        if self.is_purchased:
            print("YOU :: wow! Denim shirts is Mine")
        else:
            print("YOU :: I should earn more")
        

you = You()
you.make_payment()
