hap=0

while True:
    num=int(input("정수를 입력하시오: "))
    hap+=num
    if(num==0):
        print(f"합은 {hap} 입니다.\n")
        break
        