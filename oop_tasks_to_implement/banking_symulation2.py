'''Write a program that simulates a bank account system. 
The program should have classes for accounts, customers, and transactions. 
Accounts should have attributes such as balance, account number, and account type 
(e.g., checking, savings). Customers should have attributes such as name and contact information, 
and a list of their accounts. Transactions should have attributes such as the account involved, 
the transaction type (e.g., deposit, withdrawal), and the transaction amount. 
The program should allow customers to manage their accounts, view their transaction history, 
and transfer funds between accounts. 
Use inheritance to implement classes for different types of accounts 
(e.g., individual, business) and abstract classes for banking operations'''
from abc import ABC, abstractmethod
class Customer:
    def __init__(self, name, contact, accounts) -> None:
        self.name = name
        self.contact = contact
        self.accounts = accounts
        self.trans_history = []
        
    def view_trans_history(self):
        return self.trans_history
    
    def transfer(self, acc_number, other_acc, amount):
        for i in self.accounts:
            if int(i.number) == int(acc_number):
                i.balance -= amount
                other_acc.balance += amount
                self.trans_history.append(f'{amount} was transfered')
                
                
    def add_account(self, acc_number, balance):
        new_acc = IndividualAccount(balance, acc_number)
        self.accounts.append(new_acc)
        print(self.accounts)
                
    
class Account(ABC):
    def __init__(self, balance, number, type) -> None:
        self.balance = balance
        self.number = number
        
    @abstractmethod
    def get_type(self):
        pass
    
    def __repr__(self) -> str:
        return str((self.number, self.balance))
        
class IndividualAccount(Account):
    def __init__(self, balance, number) -> None:
        super().__init__(balance, number, 'Individual')
    
    def get_type(self):
        return 'Individual'
    
class BusinessAccount(Account):
    def __init__(self, balance, number) -> None:
        super().__init__(balance, number, 'Business')
    
    def get_type(self):
        return 'Business'
    
class Transaction:
    def __init__(self, account, trans_type, amount) -> None:
        self.account = account
        self.trans_type = trans_type
        self.amount = amount
    
    @abstractmethod    
    def make_transation(self, account, amount):
        pass
    
class Deposit(Transaction):
    def __init__(self, account, amount) -> None:
        super().__init__(account, 'Deposit', amount)
        self.make_transation(account, amount)
        
    def make_transation(self, account, amount):
        account.balance += amount
        print(f'{amount} was deposited')
        
class Withdraw(Transaction):
    def __init__(self, account, amount) -> None:
        super().__init__(account, 'Withdrawal', amount)
        self.make_transation(account, amount)
        
    def make_transation(self, account, amount):
        account.balance -= amount
        print(f'{amount} was withdrawed')
        
acc = BusinessAccount(410, 1)
acc2 = BusinessAccount(120, 2)
print(acc.get_type())
transac = Deposit(acc, 100)
customer = Customer('Mane', 'chbin', [acc])
customer.add_account(3, 500)
customer.add_account(4, 500)
customer.transfer(4, acc, 100)
customer.transfer(4, acc, 200)
customer.transfer(4, acc, 100)
print(acc.balance)
print(customer.trans_history)