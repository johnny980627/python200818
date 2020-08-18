import turtle
t = turtle.Turtle()
t2 = turtle.Turtle()
t.pencolor("lightgreen")
t.pensize(10)
t2.pensize(5)
for i in range(360):
    t.forward(1)
    t.right(1)
for i in range(360):
    t2.forward(1)
    t2.right(1)
turtle.done()