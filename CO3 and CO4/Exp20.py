class Bank_Account:
    def __init__(self):
        self.balance=0
        print("!!Welcome to the deposit and withdrawal machine!!")
    def deposit(self):
        amount=float(input("enter the amount to be deposited :"))
        self.balance+=amount
    def withdraw(self):
        amount=float(input("enter the amount to withdraw :"))
        if self.balance>=amount:
            self.balance-=amount
            print("your amount is",amount)
        else:
            print("insufficient balance")
    def display(self):
        print("available balance",self.balance)


s=Bank_Account()
s.deposit()
s.withdraw()
s.display()
