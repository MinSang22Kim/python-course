import random

user = input("가위, 바위, 보를 입력하시오: ")
com = random.choice(["가위", "바위", "보"])
print("컴퓨터:%s."%com)

if user == com:
    print("비겼습니다.")
elif (
    (user == "가위" and com == "보") or
    (user == "바위" and com == "가위") or
    (user == "보" and com == "바위")
):
    print("컴퓨터가 졌습니다.")
else:
    print("컴퓨터가 이겼습니다.")
    