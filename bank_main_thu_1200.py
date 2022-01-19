#Uzdevums
#Define a class
#Client
#name (must be given)
#timestamp (program automatically should assign value)

#Account
#account_number: assign automatically starting from 1234567890
#currency: text
#initial_balance: decimal number
#timestamp: date and time

import datetime

class Account:
    auto_account_number = 1234567890

    def __init__(self, currency: str, initial_balance: float = 0):
        self.account_number = Account.auto_account_number
        Account.auto_account_number += 1
        self.currency = currency
        self.initial_balance = initial_balance
        self.timestamp = datetime.datetime.now()

class Client:
    def __init__(self, name: str):
        self.name = name
        self.timestamp = datetime.datetime.now()
        self.accounts = []
    
    def add_account(self, account: Account):
        self.accounts.append(account)

c1 = Client('Anna')
c1.add_account(Account('EUR', 200))
c1.add_account(Account('USD', 150))
c1.add_account(Account('JPY', 4000))

