import turtle
t = turtle.Pen()
s = 0
def mysquare(size):
    for x in range(1,5):
        t.forward(size)
        t.left(90)
for i in range(1, 50):
    mysquare(s)
    s = s + 2
