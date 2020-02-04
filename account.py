import datetime
import pytz


class Account:
    """Simple account class with balance"""

    @staticmethod
    def _current_time():      # _method, are non public. non intended to be used outside class.
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self._name = name           # Attributes starting with underscore are not meant to use outside of the class.
        self.__balance = balance    # __ intended to be used in subclassing.
        self._transaction_list = [(Account._current_time(), balance)]
        print("Account created for " + self._name)
        self.show_balance()

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.show_balance()
            self._transaction_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self._transaction_list.append((Account._current_time(), -amount))
        else:
            print("Sorry. You are broke. Not enough money on the bank")
            self.show_balance()

    def show_balance(self):
        print("Balance is {}".format(self.__balance))

    def show_transactions(self):
        for date, amount in self._transaction_list:
            if amount > 0:
                transaction_type = "Deposited"
            else:
                transaction_type = "Withdrawn"
                amount *= -1
            print("{:6} {} on {} (local time was {})".format(amount, transaction_type, date, date.astimezone()))


if __name__ == '__main__':
    Emilio = Account("Emilio", 0)
    Emilio.show_balance()

    Emilio.deposit(1000)
    Emilio.withdraw(500)

    Emilio.withdraw(200)

    Emilio.show_transactions()

    Lucia = Account("Lucia", 800)
    Lucia.__balance = 200
    Lucia.deposit(100)
    Lucia.withdraw(200)
    Lucia.show_transactions()
    print(Lucia.__dict__)





