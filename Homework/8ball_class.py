import random


class eight_ball(object):
    def __init__(self, question):
        self.question = question
    def answer(self):
        l = ['Yes',
            'No',]
        n = random.randint(0, len(l)-1)
        print(l[n])
ball8 = eight_ball('Am i cool')
ball8.answer()   
