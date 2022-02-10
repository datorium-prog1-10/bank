import datetime
from turtle import settiltangle

class Transaction:
    def __init__(self, amount: float = 0, note: str = ''):
        self.amount = amount
        self.note = note
        self.timestamp = datetime.datetime.now()

class Account:
    auto_account_number = 1234567890
    
    def __init__(self, currency: str, initial_balance: float = 0):
        self._account_number = Account.auto_account_number
        Account.auto_account_number += 1
        self.transactions = []
        self.currency = currency
        self.initial_balance = initial_balance
        self.timestamp = datetime.datetime.now()

    @property #decorators    
    def account_number(self):
        return self._account_number

    def add_money(self, amount: float, note: str):
        self.transactions.append(Transaction(amount, note))

    def get_money(self, amount: float, note: str):
        self.transactions.append(Transaction(-amount, note))

    def calculate_balance(self):
        balance = self.initial_balance
        for transaction in self.transactions:
            balance += transaction.amount

        return balance

class Client:
    def __init__(self, name: str):
        self.name = name
        self.timestamp = datetime.datetime.now()
        self.accounts = []

    def add_account(self, account: Account):
        self.accounts.append(account)

    def print_accounts(self):
        print(f'Accounts of client {self.name}')
        for account in self.accounts:
            print(f'{account.account_number} ({account.currency} {account.initial_balance})')        

clients = []
clients.append(Client('Anna'))
clients.append(Client('Jenifer'))
clients.append(Client('Miki'))

clients[0].add_account(Account('EUR', 200))
clients[0].add_account(Account('USD', 150))
clients[0].add_account(Account('CAD', 300))

clients[1].add_account(Account('EUR', 800))
clients[1].add_account(Account('JPY', 10000))

clients[2].add_account(Account('EUR'))

clients[0].accounts[0].add_money(500, "Alga")
clients[0].accounts[0].get_money(100, "Veikals RIMI")
clients[0].accounts[0].get_money(50, "Restorāns Silta Saule")

print(clients[0].accounts[0].calculate_balance())