
class Bank:
    def __init__(self, name, address, balance):
        self.name = name
        self.address = address
        self.balance = balance
        self.loan = 0
        self.loan_allowed = True
    def add_balance(self, money):
        self.balance += money
    def withdraw_balance(self, money):
        self.balance -= money
    def add_loan(self, money):
        self.loan += money



        

