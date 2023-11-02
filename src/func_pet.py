from dog import Dog
from cat import Cat
from bird import Bird
from adopt_bd import MySQL_Pet_DB

class pet_functions:
    def traer_mascota(self, name):
        db_connection = MySQL_Pet_DB()  
        mascota = db_connection.traer_mascota(name)
        if mascota['race'] == "dog":
            old_pet = Dog(mascota['name'], mascota['color'], mascota['race'], mascota['ear_size'], mascota['bark'])
        elif mascota['race'] == "cat":
            old_pet = Cat(mascota['name'], mascota['color'], mascota['race'], mascota['human_hate'], mascota['meow'])
        elif mascota['race'] == "bird":
            old_pet = Bird(mascota['name'], mascota['color'], mascota['race'], mascota['wing_size'], mascota['fly_high'])
        return old_pet
        
    def crear_mascota(self, name, color, race, magnitud, attribute):
        db_connection = MySQL_Pet_DB()   
        db_connection.registrar_nueva_mascota(name, color, race, magnitud, attribute)
        
        if race == 'dog':
            new_pet = Dog(name, color, race, magnitud, attribute)
        elif race == 'cat':
            new_pet = Cat(name, color, race, magnitud, attribute)
        elif race == 'bird':
            new_pet = Bird(name, color, race, magnitud, attribute)
        return new_pet