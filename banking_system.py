class Account:
    def __init__(self, account_holder, account_number, balance=0):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew {amount}. New balance is {self.balance}.")
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        return self.balance

class SavingAccount(Account):
    def __init__(self, account_holder, account_number, balance=0, interest_rate=0.04):
        super().__init__(account_holder, account_number, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest added: {interest}. New balance is {self.balance}.")

class CurrentAccount(Account):
    def __init__(self, account_holder, account_number, balance=0, overdraft_limit=5000):
        super().__init__(account_holder, account_number, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance + self.overdraft_limit:
                self.balance -= amount
                print(f"Withdrew {amount}. New balance is {self.balance}.")
            else:
                print("Overdraft limit exceeded.")
        else:
            print("Withdrawal amount must be positive.")

class Transaction:
    def __init__(self, transaction_type, amount, account):
        self.transaction_type = transaction_type
        self.amount = amount
        self.account = account

    def process(self):
        if self.transaction_type == 'deposit':
            self.account.deposit(self.amount)
        elif self.transaction_type == 'withdraw':
            self.account.withdraw(self.amount)
        else:
            print("Invalid transaction type.")

class TransactionHistory:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def show_history(self):
        for t in self.transactions:
            print(f"{t.transaction_type.title()} of {t.amount} on account {t.account.account_number}")

customer=Account('khalil',45345,23)
customer.deposit(2000)
customer2=SavingAccount('Salman',1234,500000000000000)
customer2.add_interest()
customer2.get_balance(30)