from pet import Pet
from adopt_bd import MySQL_Pet_DB

class Bird(Pet):
    wing_size: int
    fly_high: str
    
    def __init__(self, name, color, race, wing_size, fly_high):
        db_connection = MySQL_Pet_DB()
        self.name = name
        self.color = color
        self.race = race
        self.wing_size = wing_size
        self.fly_high = fly_high
        db_connection.registrar_nueva_mascota(name, color, race, wing_size, fly_high)
        print(f'{name} fué creado con éxito!')
        
    def greet(self):
        print(self.name + " turns it´s head")