from dog import Dog
from cat import Cat
from bird import Bird

if __name__=='__main__':
    dog = Dog('babucha', 'blanco', 'poodle', 'big', 'whar!')
    cat = Cat('gatito','grey', 'persian', 'mhaw', 11)
    bird = Bird('blue', 'blue', 'loro', 'medium', 'low')
    print(vars(dog))
    print(vars(cat))
    print(vars(bird))
     
    dog.greet()
    cat.greet()
    bird.greet()