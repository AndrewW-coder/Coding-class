class Animal(object):
    def __init__(self, animal):
        self.animal = animal
    def animalnoises(self):
        print('I am', self.animal)

cheetah = Animal('Cheetah')
cheetah.animalnoises()

penguin = Animal('Penguin')
penguin.animalnoises()
