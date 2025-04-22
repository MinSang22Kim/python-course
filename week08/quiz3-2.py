import turtle;

t = turtle.Turtle()
t.shape("turtle")

radius = 50
t.fd(200)
t.left(90)
t.circle(radius)

t.fd(100)
t.left(90)
t.fd(300)
t.left(90)
t.fd(100)
t.circle(radius)
t.left(90)
t.fd(100)

turtle.done()
