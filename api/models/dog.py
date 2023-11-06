from models.pet import Pet

class Dog(Pet):
    ear_size = str
    bark = str
    
    def __init__(self, name, color, race, ear_size, bark):
        self.name = name
        self.color = color
        self.race = race
        self.ear_size = ear_size
        self.bark = bark
    
    def greet(self):
        print(self.name + " gives it´s paw")
        print("Says: " + self.bark)