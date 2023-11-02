from dog import Dog
from cat import Cat
from bird import Bird
from func_pet import pet_functions
from adopt_bd import MySQL_Pet_DB

if __name__=='__main__':
    funcs = pet_functions()
    
    Robin = funcs.traer_mascota('Robin') 
    Robin.greet()
    Zeus = funcs.crear_mascota('Khalifa', 'Brown', 'dog', 8, "whiif!")
    Zeus.greet()
