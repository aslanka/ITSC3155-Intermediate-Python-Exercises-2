class BankAccount:
    def __init__(self,account_name, starting_balance):
       self.account_name = account_name
       self.starting_balance = starting_balance
    def deposit(self,amount):
        self.starting_balance += amount
    def withdrawl(self,amount):
        self.starting_balance -= amount
    def get_balance(self):
        return str(self.account_name) + " has a balance of " + str(self.starting_balance)