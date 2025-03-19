


class Person:
    def __init__(self, account_id, first_name, last_name):
        self.account_id = account_id
        self.first_name = first_name
        self.last_name = last_name



class Account:
    def __init__(self, account_number, account_type, owner):
        self.account_number = account_number
        self.account_type = account_type
        self.owner = owner
        self.balance = float

    savings_account = []
    checking_account = []


class Bank:
    def __init__(self):
        self.account = []
        self.customer = [] #key
        self.customer_data = {}
    def withdraw_money(self, account):
        pass
    def deposit_money(self, account, deposit_money):
       pass

    def add_customer(self, customer):
        self.customer.append(customer)

    def add_account(self, account):
        self.account.append(account)

    def remove_account(self, account):
        self.account.remove(account)

    def balance_inquiry(self, account, balance_inquiry):
        pass

bob = Person(1, 'bob', 'johnson')
bob_checking = Account(400, 'Checking', bob)
bob_saving = Account(400, 'Saving', bob)
bc_bank = Bank()
bc_bank.add_customer(bob)
bc_bank.add_account(bob_checking)
bc_bank.add_account(bob_saving)
bc_bank.deposit_money(400, 19.99)
