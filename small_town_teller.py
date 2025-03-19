


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



class Bank:
    def __init__(self):
        self.accounts: dict[int, Account] = dict()
        self.customers: dict[int, Person] = dict()

    def withdraw_money(self, account_id: int, amount:float):
        if account_id in self.accounts:

    def deposit_money(self, account_id: int, amount: float):
       if account_id in self.accounts:
        account = self.accounts.get(account_id)
        account.balance += round(amount, 2)

    def add_customer(self, customer: Person):
        if customer.account_id not in self.customers:
            raise ValueError(f"Customer with id {customer.account_id} already exists.")
        else:
            self.customers[customer.account_id] = customer

    def add_account(self, account: Account):
        if account.owner.account_id not in self.customers:
            raise ValueError(f"{account.owner.account_id} is not a valid customer id.")
        elif account.account_number in self.accounts:
            raise ValueError(f"Account with id {account.account_number} already exists")

    def remove_account(self, account):
        pass

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
bc_bank.deposit_money(400, 500.95)
