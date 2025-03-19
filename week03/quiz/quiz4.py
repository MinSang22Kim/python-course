import turtle

size = int(input("사이즈를 입력하세요: "))

t = turtle.Turtle()
t.shape("arrow")
t.color("blue")
t.pencolor("red")

t.forward(size)
t.right(90)
t.forward(size)
t.right(90)
t.forward(size)
t.right(90)
t.forward(size)
t.right(90)

turtle.done()