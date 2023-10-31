from dog import Dog
from cat import Cat
from bird import Bird
from adopt_bd import MySQL_Pet_DB

if __name__=='__main__':
    db_connection = MySQL_Pet_DB()
    # dog = Dog('babucha', 'blanco', 'poodle', 'big', 'whar!')
    # cat = Cat('gatito','grey', 'persian', 'mhaw', 11)
    # bird = Bird('blue', 'blue', 'loro', 'medium', 'low')
    # print(vars(dog))
    # print(vars(cat))
    # print(vars(bird))
     
    # dog.greet()
    # cat.greet()
    # bird.greet()
    name = "Babucha"
    color = "White"
    race = "dog"
    meassure1 = 9
    attribute = "arhg!"
    
    db_connection.registrar_nueva_mascota(name, color, race, meassure1, attribute)
    
    print(db_connection.consultar_mascotas())
    