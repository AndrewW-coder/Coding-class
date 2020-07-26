class Puppy(object):
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def bark(self):
        print("I am", self.color, self.name)
puppy1 = Puppy("max", "brown")
puppy1.bark()