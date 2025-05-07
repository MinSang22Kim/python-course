a, b=0, 0
ch=" "

while True:
    print("계산기입니다!(종료하려면 연산자에 q를 입력하시오.)\n")

    a=int(input("첫번째 숫자를 입력하세요: "))
    ch=input("연산자를 입력하세요(ex: +, -, *, / )")
    if ch == "q":
        break
    b=int(input("두번째 숫자를 입력하세요: "))

    if ch == "+":
        print("%d + %d = %d" % (a, b, a+b))
    elif ch == "-":
        print("%d - %d = %d" % (a, b, a-b))
    elif ch == "*":
        print("%d * %d = %d" % (a, b, a*b))
    elif ch == "/":
        if b == 0:
            print("0으로 나눌 수 없습니다.")
        else:
            print("%d / %d = %.2f" % (a, b, a/b))
    else:
        print("잘못된 연산자입니다.")
        