import random
class User:
    def __init__(self, name,email,password,bank):
        self.name = name
        self._email = email
        self.__password = password
        self.account_number = self.generate_account_number()
        self.balance = 0
        self.transaction_history = []
        self.loan_amount = 0
        self.bank = bank

    def generate_account_number(self):
        # You can implement your logic to generate a unique account number here.
        # For simplicity, we'll use a simple counter-based approach.
        return random.randint(1,100)

    def deposit(self, amount):
        self.balance += amount
        self.bank.add_balance(amount)
        self.transaction_history.append(f"Deposited: {amount}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.bank.withdraw_balance(amount)
            self.transaction_history.append(f"Withdrew: {amount}")
        else:
            print("The bank is bankrupted")

    def transfer(self, other_user, amount):
        if self.balance >= amount:
            self.balance -= amount
            other_user.balance += amount
            self.transaction_history.append(f"Transferred: {amount} to {other_user.name}")
        else:
            print("Insufficient balance. Unable to transfer.")

    def check_balance(self):
        print(self.balance)
        return self.balance

    def get_transaction_history(self):
        print(self.transaction_history)
        return self.transaction_history

    def take_loan(self,amount):
        if self.bank.loan_allowed == True:
            if amount <= 2*self.balance and self.loan_amount == 0:
                self.loan_amount = amount
                self.balance += self.loan_amount
                self.bank.add_loan(self.loan_amount)
                self.transaction_history.append(f"Loan Taken: {self.loan_amount}")
                print(f"Loan Taken: {self.loan_amount}")
            else:
                print("You can only take a loan maximum twice your total amount and only once.")
        else:
            print("Loan is not allowed to take")

