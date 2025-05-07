hap = 0

num = int(input("숫자를 입력하시오: "))
hap += num

while True:
    ch = input("계속?(yes/no): ")
    if ch == "yes":
        num = int(input("숫자를 입력하시오: "))
        hap += num
    elif ch == "no":
        print("합계는 : ", hap)
        break
    else:
        print("잘못된 입력입니다.")
        