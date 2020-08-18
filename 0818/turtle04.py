import turtle
t = turtle.Turtle()
t.shape("turtle")
t.pu()
s=20
for i in range(30):
    t.stamp()
    s=s+3
    t.forward(s)
    t.right(24)
turtle.done()