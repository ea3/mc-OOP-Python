class Account:
    """Simple account class with balance"""

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        print("Account created for " + self.name)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.show_balance()

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            print("Sorry. You are broke. Not enough money on the bank")
            self.show_balance()


    def show_balance(self):
        print("Balance is {}".format(self.balance))


if __name__ == '__main__':
    Emilio = Account("Emilio", 0)
    Emilio.show_balance()

    Emilio.deposit(1000000)
    Emilio.deposit(1000000)
    Emilio.withdraw(4000000)


