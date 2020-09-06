import turtle
from datetime import date, datetime
from time import sleep
import datetime
import tkinter


s = turtle.Screen()
t = turtle.Turtle()
# t.hideturtle()

########################################################
class clock(object):
    def __init__(self, size):
        self.size = size
    def drawclock(self):
        t.up()
        t.setpos(0,0)
        t.dot(10)
        t.right(90)
        t.forward(self.size)
        t.right(90)
        t.right(180)
        t.down()
        t.circle(200)
        t.up()
        t.setpos(0, self.size)
        t.right(15)
        c = 0
        while c < 12:
            t.dot(5)
            t.forward(103)
            t.right(30)
            c += 1
        t.up()
        t.setpos(0, self.size+10)
        for i in range(1, 13):
            t.write(i)
            t.forward(112)
            t.right(30)

clock1 = clock(200)
clock1.drawclock()           
            
##############################################################
while True:
    today = date.today()
    t.up()
    t.setpos(-20, -20)
    t.down()
    t.write(today)
    t.up()
    t.setpos(-20, -40)
    t.down()
    current = str(datetime.datetime.now())
    hour = current[11 : 13]
    minute = current[14 : 16]
    second = current[17 : 19]
    t.undo()
    if int(hour) > 12:
        time = str(int(hour)-12) + ':' + minute + ':' + second + 'pm'
    else:
        time = hour + ':' + minute + ':' + second + 'am'
    t.write(time)
    sleep(1)
    t.undo()
###################################################################



tkinter.mainloop()