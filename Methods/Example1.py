"""
Docstring for Methods.Example1
"""

# Methods are the functions that belongs to oject

class College:

    def __init__(self, name, sec, dept):
        
        self.name = name
        self.sec = sec
        self.dept = dept

    def showDetails(self): # Class Method

        print(f" Full name : ",self.name)
        print(f" Student section : ",self.sec)
        print(f" Student Department : ",self.dept)

c = College("Alex", "B", "BBA")
c.showDetails()