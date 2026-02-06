"""
Docstring for Inheritance.Multi-Level-Inheritance.Question1

structure:
[Grandparent => Parent => Child]

Syntax:
{
class GrandParent:

    def method1(self):
        pass
    
class Parent(GrandParent):

    def method2(self):
        pass
        
class Child(Parent):

    def method3(self):
        pass
}   
"""

""" QUESTION 1 =>

Design classes:

Person → Employee → Manager

Person stores name

Employee stores employee ID

Manager stores team size
Write code to access all details using a Manager object.

"""