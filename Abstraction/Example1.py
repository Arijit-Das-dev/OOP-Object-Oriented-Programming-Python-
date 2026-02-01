"""
Docstring for Abstraction.Example

Hiding the implementation details of a class and showing the essential features to the user
"""

class Car:

    def __init__(self):
        
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self): 

        self.clutch = True
        self.acc = True
        print("Car started") # showing the essentials

car1 = Car()
car1.start()