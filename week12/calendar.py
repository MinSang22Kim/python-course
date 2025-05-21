mydic={}

while True:
    print("q를 누르면 종료합니다.")
    date = input("날짜를 입력하세요 ")
    if date == 'q': break
    job = input("일정을 입력하세요 ")

    if date not in mydic:
        mydic[date] = job
    else:
        print("오류입니다")

print(mydic)
