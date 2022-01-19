#Client class
#name
#timestamp (optional)

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
#Izveido komandā funkciju/metodi (add_account), kas pievienos klietam kontu

c1 = Client('Anna')
#print(f'{c1.name} {c1.timestamp}')

c2 = Client('Jenifer')
#print(f'{c2.name} {c2.timestamp}')

#Account
#auto_account_number (automaticly assigned starting from 1234567890)
#currency: str (teksta datu tips: 'EUR', 'PLN', 'USD')
#initial_balance: float (decimala datu tips: 100.54, 458.63)
#timestamp



a1 = Account('EUR')
print(a1.account_number)
a2 = Account('USD')
print(a2.account_number)
a3 = Account('JPY')
print(a3.account_number)