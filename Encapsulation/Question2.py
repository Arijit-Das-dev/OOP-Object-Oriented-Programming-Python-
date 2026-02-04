"""
Docstring for Encapsulation.Question2

Create an Employee class:

private salary

salary can only be updated via a method

reject salary decrease beyond a limit

"""

class Employee:

    def __init__(self, name, dept, location, salary):
        
        self.name = name
        self.dept = dept
        self.location = location
        self.__salary = salary

    def increaseSalary(self, amount):

        if amount > 0:

            self.__salary += amount
            print(f"Salary added : {amount}")
            print(f"Your salary now : {self.__salary}")
        
        else:

            print(f"Amount can not be {amount}")

    def decreaseSalary(self, amount):

        limit = 10000

        if self.__salary - amount >= limit:
            self.__salary -= amount
            print(f"Your current salary : {self.__salary}")

        else:

            print(f"You can not decrease your salary below {limit}Rs")

    def showSalaryDetails(self):

        print(f"Your current salary : {self.__salary}")

emp = Employee("Alex", "IT", "London", 30000)
emp.increaseSalary(10000)
emp.decreaseSalary(1000)