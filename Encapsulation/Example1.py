"""
Docstring for Encapsulation.Example1

Encapsulation means wrapping data and functions into single unit (object)
"""

class Account:

    def __init__(self, balance, acc_no):
        
        self.balance = balance
        self.acc_no = acc_no

    def debit(self, amount):

        if self.balance > 0:
            self.balance -= amount
        print("Total balance : ",self.showBalance())

    def credit(self, amount):

        self.balance += amount
        print("Total balance : ",self.showBalance)

    def showBalance(self):

        print(f"Account number : {self.acc_no}")
        print(f"Available balance is : {self.balance}")

a = Account(10000, 1234)
a.debit(5000)
a.credit(1000)
a.showBalance()