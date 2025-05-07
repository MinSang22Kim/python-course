pw=""
count=0
correct_pw="1234"

while True:
    pw=input("암호를 입력하세요: ")
    if pw == correct_pw:
        print("로그인 성공!")
        break

    count+=1
    
    if count >= 5:
        print("5회 이상 암호를 틀려 프로그램을 종료합니다")
        break
    else:
        continue
        