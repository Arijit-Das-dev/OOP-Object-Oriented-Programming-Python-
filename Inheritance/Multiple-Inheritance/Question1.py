"""
Docstring for Inheritance.Multiple-Inheritance.Question1

deff : Where one child class inherits from more than one parent class then it is called Multiple-Inheritance.
       In multiple inheritance parent classes does not need to inherit each other always.

Syntax:
{
class Parent1:
    pass
    
class Parent2:
    pass

class Child(Parent1, Parent2):
    pass
} 
"""

# In that case child class can perform both the operations which belongs to parent 1 and 2 alongside itself
class Parent1:

    def quality1(self):
        print("Parent 1 can sing")

class Parent2:
    
    def quality2(self):
        print("Parent 2 can dance")

class Child(Parent1, Parent2):

    def quality3(self):
        print("Child can perform both")

c = Child()
c.quality1()
c.quality2()
c.quality3()