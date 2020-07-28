class circle(object):
    def __init__(self, radius):
        self.radius = radius
    def talk(self):
        print('Since my radius is ' + str(self.radius) + '. My perimeter is ' + str(self.radius * 2 * 3.14) + '. My area is ' + str(self.radius ** 2 * 3.14))

circle1 = circle(3)
circle1.talk()
