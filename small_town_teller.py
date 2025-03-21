


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
        self.balance = 0.0



class Bank:
    def __init__(self):
        self.accounts: dict[int, Account] = dict()
        self.customers: dict[int, Person] = dict()

    def withdraw_money(self, account_id: int, amount:float):
        if account_id in self.accounts:
            account = self.accounts.get(account_id)
            account.balance -= round(amount, 2)
        else:
            raise ValueError(f"Account with id {account_id} does not exist.")

    def deposit_money(self, account_id: int, amount: float):
       if account_id in self.accounts:
        account = self.accounts.get(account_id)
        account.balance = account.balance + amount
       else:
           raise ValueError(f"Account with id {account_id} does not exist.")

    def add_customer(self, customer: Person):
        if customer.account_id in self.customers:
            raise ValueError(f"Customer with id {customer.account_id} already exists.")
        else:
            self.customers[customer.account_id] = customer

    def add_account(self, account: Account):
        if account.owner.account_id not in self.customers:
            raise ValueError(f"{account.owner.account_id} is not a valid customer id.")
        elif account.account_number in self.accounts:
            raise ValueError(f"Account with id {account.account_number} already exists")
        else:
            self.accounts[account.account_number] = account

    def remove_account(self, account: Account):
        if account.account_number not in self.accounts:
            raise ValueError(f"Account {account.account_number} does not exist")
        else:
            self.accounts[account.account_number.pop] = account

    def balance_inquiry(self, account_id,):
        if account_id in self.accounts:
            account = self.accounts.get(account_id)
            return account.balance



bc_bank = Bank()

bob = Person(1, 'bob', 'johnson')
bc_bank.add_customer(bob)
bob_saving = Account(1001, 'Saving', bob)
bc_bank.add_account(bob_saving)
bc_bank.deposit_money(1001, 19.99)
print(bc_bank.balance_inquiry(1001))


john = Person(2, 'john', 'johnson')
bc_bank.add_customer(john)
john_checking = Account(2001, 'Checking', john)
bc_bank.add_account(john_checking)
bc_bank.deposit_money(2001, 500)
bc_bank.withdraw_money(2001, 100.9)
print(bc_bank.balance_inquiry(2001))




