from pet import Pet

class Cat(Pet):
    meow = str
    human_hate = int
    
    def __init__(self, name, color, race, meow, human_hate):
        self.name = name
        self.color = color
        self.race = race
        self.meow = meow
        self.human_hate = human_hate
        
    def greet(self):
        print(self.name + " doesn´t even move")
        print("Says: " + self.meow)