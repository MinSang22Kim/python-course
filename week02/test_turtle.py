import turtle        # 터틀 그래픽 모듈 임포트

t = turtle.Turtle()  # 터틀 객체 생성
t.shape("square")    # 터틀 모양 변경
t.color("blue")      # 터틀 색 변경
t.pencolor("red")    # 펜 색 변경

t.circle(100)        # 반지름 100짜리 원 그리기

t.penup()            # 펜 들기 (선 안 그림)
t.fd(200)            # 앞으로 200 이동
t.pendown()          # 펜 내리기 (그리기 시작)

t.pencolor("orange") # 펜 색 변경
t.circle(150)        # 반지름 150짜리 원 그리기

# 사각형 그리기
for _ in range(4):  
    t.forward(100)   # 앞으로 100 이동
    t.left(90)       # 왼쪽으로 90도 회전

# 삼각형 그리기
for _ in range(3):  
    t.forward(100)   # 앞으로 100 이동
    t.left(120)      # 왼쪽으로 120도 회전

turtle.done()        # 창이 닫히지 않도록 유지