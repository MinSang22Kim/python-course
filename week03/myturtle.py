import turtle

t=turtle.Turtle()
t.shape("turtle")
radius=70

for _ in range(6):
    t.circle(radius)
    t.fd(100)

turtle.done()
