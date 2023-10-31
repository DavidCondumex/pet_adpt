from pet import Pet

class Cat(Pet):

    def __init__(self, name, color, race, human_hate, meow):
        self.name = name
        self.color = color
        self.race = race
        self.meow = meow
        self._human_hate = human_hate
        
    def greet(self):
        print(self.name + " doesn´t even move")
        print("Says: " + self.meow)
        
    @property
    def human_hate(self, value):
        self._human_hate = value
        
    @human_hate.setter
    def human_hate(self, value):
        if value > 10:
            print("We can't meassure more than 10 hate points")
        else:
            print("Setting hate...")
            self._human_hate = value
    
    @human_hate.getter
    def human_hate(self, value):
        return self._human_hate
        