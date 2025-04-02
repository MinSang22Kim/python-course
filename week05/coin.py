import random

print("동전 던지기 게임")
coin=random.randrange(2)

if coin==0:
    print("동전은 앞면입니다.")
else:
    print("동전은 뒷면입니다.")

print("동전 던지기 게임 종료")
