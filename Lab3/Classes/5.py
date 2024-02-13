class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount): #положить
        if amount > 0:
            self.balance += amount
            print("Deposit is ", amount, "New balance: ", self.balance) 
        else:
            print("Deposit amount must be greater than 0.")

    def withdraw(self, amount):          #снять
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print ("Withdraw is ", amount , "New balance: ", self.balance)
            else:
                print("No enough Money")

x=int(input())
y=int(input())    
a=int(input())
b=int(input())
c=int(input())
d=int(input())

my_account = Account(x, y)

   
my_account.deposit(a)
my_account.deposit(b)

    
my_account.withdraw(c)
my_account.withdraw(d)