"""BankAccout and transfer."""


class BankAccount:
    """BankAccount."""

    def __init__(self, name, balance):
        """A."""
        self.name = name
        self.balance = balance
        if self.balance < 0:
            self.balance = 0

    def withdraw(self, amount):
        """A."""
        if amount > self.balance or amount < 0:
            return False
        self.balance -= amount
        return True

    def deposit(self, amount):
        """A."""
        if amount > 0:
            self.balance += amount
        else:
            self.balance = self.balance

    def get_balance(self):
        """A."""
        return self.balance

    def get_name(self):
        """A."""
        return self.name

    def transfer(self, target, amount, fee=0.01):
        """A."""
        if target is None:
            return False
        if amount < 0:
            return False
        if self == target:
            fee = 0
        elif self.get_name() == target.get_name():
            fee /= 2
            print(fee)
        if self.get_balance() >= amount * (1 + fee):
            target.deposit(amount)
            self.withdraw(amount * (1 + fee))
            return True
        else:
            return False
