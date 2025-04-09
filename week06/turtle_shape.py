import turtle

t=turtle.Turtle()
t.shape("circle")

s=turtle.textinput("도형그리기", "도형을 입력하세요: ")
if s=="사각형":
    s=turtle.textinput("", "가로크기: ") # 단위: px
    w=int(s)
    s=turtle.textinput("", "세로크기: ")
    h=int(s)

    t.fd(w)
    t.left(90)
    
    t.fd(h)
    t.left(90)

    t.fd(w)
    t.left(90)

    t.fd(h)
    t.left(90)

elif s=="삼각형":
    s=turtle.textinput("", "한 변의 길이: ")
    l=int(s)

    t.fd(l)
    t.left(120)
    
    t.fd(l)
    t.left(120)
    
    t.fd(l)
    t.left(120)

elif s=="원형":
    s=turtle.textinput("", "반지름의 길이: ")
    r=int(s)
    
    t.circle(r)

else:
    pass
turtle.done()
