import turtle

t = turtle.Turtle()
colors=["red", "orange", "yellow", "green", "blue", "purple"]

turtle.bgcolor("black")
t.speed(10)
t.width(5)

num=int(turtle.textinput("진짜 멋진 다각형 그리기", "몇각형을 원하시나요?"))
for i in range(num):
    t.pencolor(colors[i % len(colors)])
    t.fd(100)
    t.left(360//num)

turtle.done()
