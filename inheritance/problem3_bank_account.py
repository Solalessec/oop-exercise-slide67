"""Inheritance - Problem 3.

BankAccount (deposit, withdraw, transfer) and SavingsAccount
(adds interest_rate, add_interest and check_balance).
"""


class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount

    def transfer(self, destination, amount):
        """Move money to another account.

        Returns False if the balance is insufficient, True otherwise.
        """
        if amount > self.balance:
            return False
        self.withdraw(amount)
        destination.deposit(amount)
        return True


class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance=0, interest_rate=0.03):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate  # e.g. 0.03 = 3 %

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return interest

    def check_balance(self):
        return self.balance


if __name__ == "__main__":
    current = BankAccount("FR-001", 500)
    savings = SavingsAccount("FR-002", 1000, interest_rate=0.05)

    current.deposit(200)
    current.withdraw(100)
    print(f"Current account balance: {current.balance}")  # 600

    print(f"Transfer 250 to savings: {current.transfer(savings, 250)}")   # True
    print(f"Transfer 5000 to savings: {current.transfer(savings, 5000)}")  # False

    interest = savings.add_interest()
    print(f"Interest added: {interest}")
    print(f"Savings balance: {savings.check_balance()}")  # (1000 + 250) * 1.05 = 1312.5
