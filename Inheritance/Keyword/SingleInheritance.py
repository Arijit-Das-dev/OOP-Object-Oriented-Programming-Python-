"""
Docstring for Inheritance.Keyword.SingleInheritance
"""

class Engine:

    def __init__(self, eng_type, eng_cap, num_cyl, fuel_type, hp, tor):
        
        self.eng_type = eng_type
        self.eng_cap = eng_cap
        self.num_cyl = num_cyl
        self.fuel_type = fuel_type
        self.hp = hp
        self.tor = tor

class BMW(Engine):

    def __init__(self, eng_type, eng_cap, num_cyl, fuel_type, hp, tor):
        super().__init__(eng_type, eng_cap, num_cyl, fuel_type, hp, tor)

car1 = BMW("Petrol", "1197cc", 8, "Petrol", "Engine power output", "Twisting force")
print(car1.eng_cap, car1.eng_type, car1.fuel_type, car1.hp, car1.num_cyl, car1.tor)