import turtle

t = turtle.Turtle()
t.shape("square")

t.color("blue")
t.pencolor("red")

t.circle(100)

t.penup()
t.fd(200)
t.pendown()

t.pencolor("orange")
t.circle(150)

# 사각형 그리기
for _ in range(4):
    t.forward(100)
    t.left(90)

# 삼각형 그리기
for _ in range(3):
    t.forward(100)
    t.left(120)

turtle.done()
turtle.done()