"""
Docstring for Constructors.Example2
"""

class Name:

    def __init__(self, fullName, marks):
        
        self.fullName = fullName # fullName is an attribute of the class
        self.marks = marks
        print("New name added")

n = Name("A", 12)
print(n.fullName, n.marks)