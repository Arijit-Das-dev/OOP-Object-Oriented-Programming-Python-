"""
Docstring for Methods.Practice

QS: Create student class that takes name & marks of 3 subjects as arguements in constructor.
    Then create a method to print the average
"""

class Student: 

    def __init__(self, name, marks):

        self.name = name
        self.marks = marks

    def showDetails(self):

        print(f"Student name : {self.name}\n Student marks :{self.marks}")

    def average(self):

        summ = 0

        for marks in self.marks:

            summ += marks

        print(f"Average marks : {round(summ/len(self.marks), 2)}")

s1 = Student("Adam", [12, 23, 56])
s1.showDetails()
s1.average()