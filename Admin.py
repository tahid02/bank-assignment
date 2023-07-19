class Admin:
    def __init__(self, admin_name, email, password, bank):
        self.admin_name = admin_name
        self.__email = email
        self.__password = password
        self.bank = bank

    def check_balance(self):      
        print(f"Bank Balance is {self.bank.balance}")
        return self.bank.balance

    def check_loan(self):
        print('loan in bank is ',self.bank.loan)

    def on_off_loan(self, allow_loan):
        self.bank.loan_allowed = allow_loan
        print('loan is allowed ',self.bank.loan_allowed) 

