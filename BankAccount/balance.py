from BankAccount import account
 

account = account.Account("balance.txt")
print(account.balance)
account.withdraw(100)
print(account.balance)
account.commit()

