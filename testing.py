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

c1 = Client('Ivo')
c1.add_account(Account('EUR', 200))
c2 = Client('Walker #71391')
c3 = Client('Joe')
#print(f'{c1.name} {c1.timestamp}')

a1 = Account('EUR', 200)
a2 = Account('RUB', 100000)
a3 = Account('USD', 350)

print(f'{c1.name} {a1.account_number} {a1.currency} {a1.initial_balance} {a1.timestamp}')
print(f'{c2.name} {a2.account_number} {a2.currency} {a2.initial_balance} {a2.timestamp}')
print(f'{c3.name} {a3.account_number} {a3.currency} {a3.initial_balance} {a3.timestamp}')