import turtle
t = turtle.Pen()
s = 0
c = 0
def mysquare(size):
    for x in range(1,5):
        t.forward(size)
        t.left(90)
def mycircle(size):
    t.circle(c)
for i in range(1, 50):
    mysquare(s)
    mycircle(c)
    s = s + 2
    c = c + 10
turtle.done()
