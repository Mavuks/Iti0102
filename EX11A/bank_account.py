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

    def transfer(self, target, amount, fee = 0.01):
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




if __name__ == '__main__':

    mary_account = BankAccount("Mary", 100)
    guido_account = BankAccount("Guido", 150)
    mary_second_account = BankAccount("Mary", 78.01)

    # float comparison
    assert abs(mary_account.get_balance() - 100) < 0.001
    assert abs(mary_second_account.get_balance() - 78.01) < 0.001
    assert abs(guido_account.get_balance() - 150) < 0.001

    assert mary_account.get_name() == "Mary"
    assert guido_account.get_name() == "Guido"
    assert mary_second_account.get_name() == "Mary"

    mary_account.deposit(10)
    assert abs(mary_account.get_balance() - 110) < 0.001
    mary_account.deposit(-10)
    assert abs(mary_account.get_balance() - 110) < 0.001
    assert mary_account.withdraw(-10) is False
    assert abs(mary_account.get_balance() - 110) < 0.001
    assert mary_account.withdraw(1000) is False
    assert abs(mary_account.get_balance() - 110) < 0.001
    assert mary_account.withdraw(10) is True
    assert abs(mary_account.get_balance() - 100) < 0.001

    assert mary_account.transfer(guido_account, 10) is True
    assert abs(mary_account.get_balance() - 89.9) < 0.001
    assert abs(guido_account.get_balance() - 160) < 0.001

    print("Add asserts for transferring between the accounts of the same owner")
    print("Add asserts for transferring between the same account")
    # TODO: Add asserts for transferring from mary_account to mary_second_account
    # and from mary_account to mary_account
    # asserts for transferring between the same account
    assert mary_account.transfer(mary_account, 10, 1000) is True
    assert abs(mary_account.get_balance() - 89.9 < 0.001)
    # asserts for transferring between the accounts of the same owner
    assert mary_account.transfer(mary_second_account, 10, 10) is True
    assert abs(mary_account.get_balance() - 29.9 < 0.001)
    assert abs(mary_second_account.get_balance() - 88.01 < 0.001)
    # test_transfer_to_non_existing_account
    mary_acc = 0
    assert mary_account.transfer(mary_acc, 10, 10) is False
    # test transfer neg amount
    assert mary_account.transfer(mary_account, -10, 10) is False
    # test transfer 0 and neg fee
    assert mary_account.transfer(guido_account, 0, -1) is True
    print("And now you are ready for submission!")
    assert False

    print("And now you are ready for submission!")
