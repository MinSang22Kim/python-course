while True:
    num1 = int(input("시작값을 입력하세요: "))
    num2 = int(input("끝값을 입력하세요: "))
    num3 = int(input("증가값을 입력하세요: "))
    
    if num2==0 or num3==0:
        print("끝값 or 증가값으로 0이 입력되었습니다. 프로그램을 종료합니다.\n")
        break
    elif num1 > num2:
        print("시작값이 끝값보다 큽니다. 다시 입력하세요.\n")
        continue
    elif num3 < 0:
        print("증가값은 0보다 커야 합니다. 다시 입력하세요.\n")
        continue
    elif num1 == num2:
        print("시작값과 끝값이 같습니다. 다시 입력하세요.\n")
        continue

    hap = 0
    for i in range(num1, num2+1, num3):
        hap += i
    print(f"{num1}에서 {num2}까지 {num3}씩 증가시킨 값의 합계: {hap}\n")
