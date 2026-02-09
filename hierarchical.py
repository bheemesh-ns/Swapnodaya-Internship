#Hierarchical Inheritance 

class Bank_account:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. Remaining balance: {self.balance}")    
    def display_balance(self):
        print(f"Balance: {self.balance}")        

class SavingAccount(Bank_account):
    def __init__(self, account_holder, balance, interest_rate):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate
    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        print(f"Added interest: {interest}. New balance: {self.balance}")

class CurrentAccount(Bank_account):
    def __init__(self, account_holder, balance, overdraft_limit):
        super().__init__(account_holder, balance)
        self.overdraft_limit = overdraft_limit
    def withdraw_with_overdraft(self, amount):
        if amount > self.balance + self.overdraft_limit:
            print("Overdraft limit exceeded")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. Remaining balance: {self.balance}")

obj = SavingAccount("Alice", 1000, 5)
obj.deposit(500)
obj.add_interest()
obj.display_balance()

obj2 = CurrentAccount("Bob", 2000, 500)
obj2.withdraw_with_overdraft(2500)
obj2.display_balance()
