from dog import Dog
from cat import Cat
from bird import Bird
from adopt_bd import MySQL_Pet_DB

def consultar_mascota(self, name):
    mascota = db_connection.traer_mascota(name)
    if mascota.race == "dog":
        old_pet = Dog(mascota.name, mascota.color, mascota.race, mascota.ear_size, mascota.bark)
    elif mascota.race == "cat":
        old_pet = Cat(mascota.name, mascota.color, mascota.race, mascota.human_hate, mascota.meow)
    elif mascota.race == "bird":
        old_pet = Bird(mascota.name, mascota.color, mascota.race, mascota.wing_size, mascota.fly_high)
    return old_pet

if __name__=='__main__':

    db_connection = MySQL_Pet_DB()
    name = "Nala"
    color = "Brown"
    race = "dog"
    meassure1 = 4
    attribute = "Wooogh!"
    
    # Pongo = Dog("Pongo", "Grey", "dog", 7, "Furghrr!")
    
    # MiniG = Cat("MiniG", "Black", "cat", 2, "mowh!")
    
    # Abelardo = Bird("Abelardo", "Green", "bird", 10, "Hola!")
    
    # Pongo.greet()
    # MiniG.greet()
    # Abelardo.greet()
    
    # Robin = consultar_mascota("Robin")
    
    # Robin.greet()
    
    mascota = db_connection.traer_mascota(name)
    print(mascota)
    # if mascota.race == "dog":
    #     old_pet = Dog(mascota.name, mascota.color, mascota.race, mascota.ear_size, mascota.bark)
    # elif mascota.race == "cat":
    #     old_pet = Cat(mascota.name, mascota.color, mascota.race, mascota.human_hate, mascota.meow)
    # elif mascota.race == "bird":
    #     old_pet = Bird(mascota.name, mascota.color, mascota.race, mascota.wing_size, mascota.fly_high)
    # old_pet.greet()