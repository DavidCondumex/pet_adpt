from pet import Pet

class Bird(Pet):
    wing_size: int
    fly_high: str
    
    def __init__(self, name, color, race, wing_size, fly_high):
        self.name = name
        self.color = color
        self.race = race
        self.wing_size = wing_size
        self.fly_high = fly_high
        
    def greet(self):
        print(self.name + " turns it´s head")