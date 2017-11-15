"""BankAccout and transfer."""


class BankAccount:
    """BankAccount."""


    def __init__(self, name, balance):
        """A."""
        self.name = name
        self.balance = balance

    def withdraw(self, amount):
        """A."""
        if amount > self.balance:
            return False
        if amount < 0:
            return False
        self.balance -= amount
        return True

    def deposit(self, amount):
        """A."""
        if amount > 0:
            self.balance += amount
        else:
            pass



    def get_balance(self):
        """A."""
        return self.balance
    def get_name(self):
        """A."""
        return self.name

    def transfer(self, target, amount, fee):
        """A."""


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
    assert mary_account.withdraw(-10) == False
    assert abs(mary_account.get_balance() - 110) < 0.001
    assert mary_account.withdraw(1000) == False
    assert abs(mary_account.get_balance() - 110) < 0.001
    assert mary_account.withdraw(10) == True
    assert abs(mary_account.get_balance() - 100) < 0.001

    assert mary_account.transfer(guido_account, 10) == True
    assert abs(mary_account.get_balance() - 89.9) < 0.001
    assert abs(guido_account.get_balance() - 160) < 0.001

    print("Add asserts for transferring between the accounts of the same owner")
    print("Add asserts for transferring between the same account")
    # TODO: Add asserts for transferring from mary_account to mary_second_account
    # and from mary_account to mary_account
    assert False

    print("And now you are ready for submission!")
