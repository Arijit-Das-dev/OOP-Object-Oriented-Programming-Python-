"""
Docstring for Constructors.Default&ParameterizedConstructor
"""

class Example:

    def __init__(self): # Default constructor
        pass

    def __init__(self, FirstName, LastName): # Parameterized constructor

        self.FirstName = FirstName
        self.LastName = LastName

e = Example("Arijit", "Das")
print(e.FirstName, e.LastName)