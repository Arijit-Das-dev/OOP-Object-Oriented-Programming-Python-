"""
Docstring for Encapsulation.validationTypeQuestions.Question1

=> Create a class where age must be between 18–60.

"""

class AgeInput:

    def __init__(self):
        
        self.__validateAge = True
        self._ageList = []

    def inputAge(self, age):

        if 18 <= age <= 60:

            self.__validateAge
            self._ageList.append(age)
            print(f"Age added successfully.")

        else:

            self.__validateAge = False
            print("Age is not acceptable !")
        
    def showAge(self):

        return self._ageList
    
age = AgeInput()
age.inputAge(90)
age.inputAge(45)
print(age.showAge())