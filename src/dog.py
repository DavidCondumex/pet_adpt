from pet import Pet
from adopt_bd import MySQL_Pet_DB

class Dog(Pet):
    ear_size = str
    bark = str
    
    def __init__(self, name, color, race, ear_size, bark):
        db_connection = MySQL_Pet_DB()
        self.name = name
        self.color = color
        self.race = race
        self.ear_size = ear_size
        self.bark = bark
        db_connection.registrar_nueva_mascota(name, color, race, ear_size, bark)
        print(f'{name} fué creado con éxito!')
    
    def greet(self):
        print(self.name + " gives it´s paw")
        print("Says: " + self.bark)