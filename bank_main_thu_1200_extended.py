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
        print(f'Accounts for client {self.name}')
        for acc in self.accounts:
            print(f'{acc.account_number} ({acc.currency} {acc.initial_balance})')


c1 = Client('Anna')
c2 = Client('Jenifer')
c3 = Client('Miki')

c1.add_account(Account('EUR', 200))
c1.add_account(Account('USD', 150))
c1.add_account(Account('JPY', 4000))

#hack and delete Anna's USD account
c1.accounts.pop(1)

c2.add_account(Account('EUR', 800))
c2.add_account(Account('SEK', 70000))

c1.print_accounts()
c2.print_accounts()
c3.print_accounts()