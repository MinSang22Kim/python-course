import turtle

t = turtle.Turtle()
t.shape("turtle")
t.color("blue")
t.pencolor("red")
size = int(input("사이즈를 입력하시오: "))

for _ in range(4):
    t.fd(size)
    t.left(90)

turtle.done()
