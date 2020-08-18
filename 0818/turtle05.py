import turtle
t = turtle.Turtle()
l = int(input("邊數:"))
for i in range(l):
    t.forward(20)
    t.right(360/l)