import random

win=random.randrange(0, 100)
num=int(input("복권번호를 입력하시오(0~99): "))
print("당첨번호는 %d입니다."%win)
if num==win:
    print("100만원 당첨!")
elif num%10==win//10 or num%10==win%10 or num//10==win%10 or num//10==win//10:
    print("50만원 당첨!")
else:
    print("꽝!")
    