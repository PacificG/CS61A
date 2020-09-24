class Account:
    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return self.balance

class checkingAccount(Account):
    withdraw_charge = 1
    interest_rate = 0.01
    def withdraw(self, balance):
        return Account.withdraw(self, balance + self.withdraw_charge)

    