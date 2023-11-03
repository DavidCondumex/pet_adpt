from func_pet import pet_functions
from time import sleep

if __name__=='__main__':
    funcs = pet_functions()
    option = int
    while option != 5:
        option = int(input('''
                        1.-Nueva Mascota
                        2.-Llamar a una mascota
                        3.-Lista de mascotas
                        4.-Adoptar una mascota
                        5.-Salir
                        '''))

        if option == 1:
            name = input("Intoduce el nombre de la mascota: ")
            color = input("Cuál es el color de la mascota? ")
            raza = input("Es de tipo dog, cat o bird? ")
            magnitud = input("Cuál es el tamaño de orejas, odio a humanos o tamaño de alas según el caso? ")
            attributo = input("Cuál es su sonido o altura de vuelo según el caso? ")
            nuevo = funcs.crear_mascota(name, color, raza, magnitud, attributo)
            nuevo.greet()
            sleep(3)
        elif option == 2:
            name = input("A quién deseas traer? ")
            traido = funcs.traer_mascota(name)
            traido.greet()
        elif option == 3:
            funcs.lista_mascotas()
            sleep(3)
        elif option == 4:
            name = input("Quién será adoptado? ")
            funcs.adoptar_mascota(name)
            sleep(3)
        elif option == 5:
            print("Bye bye!")
        else:
            print("Lo siento, no reconozco esa opción")