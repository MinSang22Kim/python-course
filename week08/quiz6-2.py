import turtle

t=turtle.Turtle()

t.penup()
t.goto(100, 100)
t.write("양수입니다.")
t.goto(100, 0)
t.write("0입니다.")
t.goto(100, -100)
t.write("음수입니다.")

t.goto(0,0)
t.pendown()

num=int(turtle.textinput("입력", "숫자를 입력하시오: "))
if num>0:
    print("양수입니다.")
    t.pencolor("blue")
    t.goto(100, 100)
elif num==0:
    print("0입니다.")
    t.goto(100, 0)
else:
    print("음수입니다.")
    t.pencolor("red")
    t.goto(100, -100)

turtle.done()
