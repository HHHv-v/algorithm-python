class Bank:
    def __init__(self,account_id,balance):
        self.account_id=account_id
        self.balance=balance
        
    def deposit(self,amount):
        self.balance+=amount
    
    def withdraw(self,amount):
        if amount>self.balance:
            return False
        self.balance-=amount
        return True      

n=int(input())
bank={}

for _ in range(n):
    account, balance=input().split()
    bank[account]=Bank(account,int(balance))

q=int(input())
commands=[input().split() for _ in range(q)]

for operation, *operands in commands:
    if operation == "DEPOSIT":
        account=bank[operands[0]]
        account.deposit(int(operands[1]))
        print(account.balance)
    
    elif operation == "WITHDRAW":
        account=bank[operands[0]]
        if account.withdraw(int(operands[1])):
            print(account.balance)
        else:
            print("FAIL", account.balance)
    
    elif operation == "TRANSFER":
        sender, receiver = bank[operands[0]],bank[operands[1]]
        amount=int(operands[2])
        if sender.withdraw(amount):
            receiver.deposit(amount)
            print("OK", sender.balance, receiver.balance)
        else:
            print("FAIL", sender.balance, receiver.balance)
    
    elif operation == "BALANCE":
        print(bank[operands[0]].balance)