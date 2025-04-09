## 수평선 기준으로 수가 양수이면 위, 음수이면 아래
import turtle

t=turtle.Turtle()
t.shape("classic")

t.penup()
t.goto(100, 100)
t.write("양수의 자립니다.")

t.goto(100, 0)
t.write("0의 자립니다.")

t.goto(100, -100)
t.write("음수의 자립니다.")

t.goto(0,0)
t.pendown()
s=turtle.textinput("test", "숫자를 입력하시오")
n=int(s)

if n>0:
    t.color("yellow")
    t.pencolor("blue")
    t.goto(100, 100)
elif n==0:
    t.goto(100, 0)
elif n<0:
    t.color("yellow")
    t.pencolor("red")
    t.goto(100, -100)
else:
    pass

turtle.done()
