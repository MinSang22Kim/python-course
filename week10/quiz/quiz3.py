import random

print("1부터 100 사이의 숫자를 맞히시오")
goal=random.randint(1, 100)

while True:
    num=int(input("숫자를 입력하시오: "))
    if num<1 or num>100:
        print("1부터 100 사이의 숫자를 입력하시오")
        continue
    elif num == goal:
        print("정답!")
        break
    elif num < goal:
        print("낮음!")
    else:
        print("높음!")
