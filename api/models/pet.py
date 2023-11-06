from models.eyes import Eyes

class Pet():
    name = str
    color = str
    race = str
    eyes = None
    
    def __init__(self, name, color, race):
        self.name = name
        self.color = color
        self.race = race
        self._eyes = Eyes('green', 'little', 'sides')
        

        



        
