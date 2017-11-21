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
        if self.balance >= amount:
            if self.get_name() == target.get_name():
                fee = fee / 2
            elif self == target:
                fee = 0
            target.balance = target.deposit(amount)
            self.balance = self.withdraw(amount * (1 + fee))
            print(target.get_balance())
            print(self.get_balance())
            return True
        else:
            return False

