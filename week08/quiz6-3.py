import turtle

t=turtle.Turtle()
s = turtle.textinput("", "원하는 도형을 입력하시오: ")

if s=="사각형":
    s=int(turtle.textinput("", "가로길이는? "))
    h=int(turtle.textinput("", "높이는? "))
    t.fd(s)
    t.left(90)
    t.fd(h)
    t.left(90)
    t.fd(s)
    t.left(90)
    t.fd(h)
    t.left(90)
elif s=="삼각형":
    size=int(turtle.textinput("", "한변길이는? "))
    for _ in range(3):
        t.fd(size)
        t.left(120)
elif s=="원형":
    radius=int(turtle.textinput("", "반지름은? "))
    t.circle(radius)
else:
    pass

turtle.done()
