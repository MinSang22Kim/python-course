import random

win = random.randint(10, 99)
num = int(input("복권번호를 입력하세요(0에서 99사이): "))
print("당첨번호는 %d입니다." % win)

if num == win:
    print("100만원 당첨입니다.")
elif (num % 10 == win % 10) or (num // 10 == win // 10) or (num % 10 == win // 10) or (num % 10 == win // 10):
    print("50만원 당첨입니다.")
else:
    print("상금은 없습니다.")
