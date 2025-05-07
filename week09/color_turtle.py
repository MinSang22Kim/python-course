import turtle

t = turtle.Turtle()
colors=["red", "green", "blue"]

turtle.bgcolor("black")
t.speed(0)
t.width(3)

length=10

for i in range(200):
    t.fd(length)
    t.pencolor(colors[length%3])
    t.right(99)
    length +=5

turtle.done()
