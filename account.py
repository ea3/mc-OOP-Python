import datetime
import pytz


class Account:
    """Simple account class with balance"""

    @staticmethod
    def _current_time():      # _method, are non public. non intended to be used outside of the class. STATIC METHOD, USE THE CLASS TO ACCESS THEM 
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transaction_list = []
        print("Account created for " + self.name)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.show_balance()
            self.transaction_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_list.append((Account._current_time(), -amount))
        else:
            print("Sorry. You are broke. Not enough money on the bank")
            self.show_balance()

    def show_balance(self):
        print("Balance is {}".format(self.balance))

    def show_transactions(self):
        for date, amount in self.transaction_list:
            if amount > 0:
                transaction_type = "Deposited"
            else:
                transaction_type = "Withdrawn"
                amount *= -1
            print("{:6} {} on {} (local time was {})".format(amount, transaction_type, date, date.astimezone()))


if __name__ == '__main__':
    Emilio = Account("Emilio", 0)
    Emilio.show_balance()

    Emilio.deposit(1000000)
    Emilio.deposit(1000000)
    Emilio.withdraw(500000)

    Emilio.show_transactions()



