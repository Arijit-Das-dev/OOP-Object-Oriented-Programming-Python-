"""
Docstring for Encapsulation.Protected
"""

# Protected method
# represented by single underscore

class PrivateMethod:

    def __init__(self):

        self._acc_num = 1234
    
p = PrivateMethod()
print(p._acc_num)