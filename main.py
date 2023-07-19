from Bank import Bank
from Admin import Admin
from User import User

def main():
             
    bank = Bank('Safe Bank', '123 Main Street', 100) # ( bank name, address, initial balance)
    admin = Admin('Admin1', 'admin1@gmail.com', 'admin1', bank) #(admin name, email, password)
    admin.check_balance()  # initial balance is 100
    admin.check_loan() # loan in bank is 0

    user1 = User("John",'john@gmail.com','johnPass',bank)
    user2 = User("Jane",'jane@gmail.com','janePass',bank)


    # user deposit and withdraw

    user1.deposit(1000)
    print('user 1 balance',user1.balance)
    print('current  balance of bank',bank.balance)

    user1.withdraw(500)
    print('user 1 balance',user1.balance)
    print('current  balance of bank',bank.balance)

    user2.deposit(2000)
    print('user 2 balance',user2.balance)
    print('current  balance of bank',bank.balance)

    #  transfer balance
    user1.transfer(user2, 300)
    print("User 1 Balance:", user1.check_balance())
    print("User 2 Balance:", user2.check_balance())
    print("User1 Transaction History:", user1.get_transaction_history())
    print("User2 Transaction History:", user2.get_transaction_history())

    # user taking loan from bank
    user1.take_loan(200)
    print('user 1 balance',user1.balance)
    print('current loan in bank',bank.loan)
    user1.take_loan(4500000) # output: You can only take a loan maximum twice your balance and only once

    admin.on_off_loan(False) # loan off
    user2.take_loan(100) # output: loan is not allowed to take 




if __name__ == '__main__':
    main()