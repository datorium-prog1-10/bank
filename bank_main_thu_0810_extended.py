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

    def print_accounts(self):
        print(f'All acounts of client {self.name}')
        for a in self.accounts:
            print(f'{a.account_number} ({a.currency} {a.initial_balance})')

#UZDEVUMS
#Izveido klientam funkciju/metodi print_accounts kas izvada visus
#klienta konta numurus

#PIEMĒRS:
#All acounts of client Anna
#1234567890 (EUR 500)
#1234567891 (USD 200)
#1234567892 (JPY 4000)

c1 = Client('Anna')
c2 = Client('Jenifer')

c1.add_account(Account('EUR', 500))
c1.add_account(Account('USD', 200))
c1.add_account(Account('JPY', 4000))

c1.print_accounts()

#uzhako Annas kontu un izdzēš USD kontu
c1.accounts.pop(1)
c1.print_accounts()