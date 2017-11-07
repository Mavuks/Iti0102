"""Simple bank."""


class Account:
    """Represent a bank account."""

    def __init__(self, name, balance):
        """
        Class constructor. Each account has owner's name and starting balance.

        :param name: account owner name. String.
        :param balance: starting balance of account. Integer.
        """
        self.name = name
        self.balance = balance


    def withdraw(self, amount):
        """
        Withdraw money from account.

        :param amount: amount to withdraw from account, has to be positive
        and the balance can't go below 0.
        """


    def deposit(self, amount):
        """
        Deposit money to account.

        :param amount: amount to deposit to account, has to be positive
        """
        pass

    def get_balance(self):
        """
        Get account balance.

        :return: balance in double form
        """
        return self.balance

    def get_name(self):
        """
        Get account owner name.

        :return: owner name in string form
        """
        return self.name

    paul_account = Account("Paul", 100.00)
    jakob_account = Account("Jakob", 500.00)

    print("Initial balance")
    print(paul_account.get_balance())  # 100.0
    print(jakob_account.get_balance())  # 500.0