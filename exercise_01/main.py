from BankAccount import BankAccount

account_1 = BankAccount("Account1", 1000)
account_1.deposit(500)
account_1.withdrawl(400)
print(account_1.get_balance())