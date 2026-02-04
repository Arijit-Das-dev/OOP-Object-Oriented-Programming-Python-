"""
Docstring for Encapsulation.Question4

Create a Wallet class where balance cannot go negative.
"""

class Wallet:

    def __init__(self, balance):

        self.__balance = balance
        self.isNegative = False
    
    def addBalance(self, amount):

        if amount <= 0:
            print("Amount can not be zero")
            return
        
        if amount > 0:
            self.__balance += amount
        print(f"Balance : {amount} Rs added to your account.")
        print(f"Your available balance : {self.__balance} Rs")
    
    def withDraw(self, amount):

        if amount <= 0:
            print("Amount can not be zero")
            return
        
        if amount > self.__balance:
            print("Insufficient balance")
            return
        
        self.__balance -= amount
        print(f"Your available balance is : {self.__balance}")
    
    def showDetails(self):

        return f"Your available balance is : {self.__balance}"

w = Wallet(15000)
w.addBalance(5000)
w.withDraw(40000)