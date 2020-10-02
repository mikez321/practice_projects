"""Bank Account with a balance."""


class Account:
    """Simple account class with balance."""

    def __init__(self, name, balance):
        """Create a bank account with balance and owner name."""
        self.name = name
        self.balance = balance
        print("Account created for {}".format(self.name))

    def deposit(self, amount):
        """Add to the existing balance."""
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        """Lower the current balance."""
        if self.balance <= amount:
            self.balance -= amount

    def show_balance(self):
        """Show the current balance."""
        print("Balance is {}".format(self.balance))


if __name__ == '__main__':
    account = Account('Mike', 100)
    account.show_balance()
    account.deposit(25)
    account.show_balance()
    account.withdraw(100)
    account.show_balance()
