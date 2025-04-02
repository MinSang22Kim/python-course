correct_id = "KUTIS"
correct_pw = "12345"

user_id = input("아이디를 입력하세요: ")
if user_id == correct_id:
    user_pw = input("패스워드를 입력하세요: ")
    if user_pw == correct_pw:
        print("환영합니다.")
    else:
        print("비밀번호가 잘못되었습니다.")
else:
    print("아이디를 찾을 수 없습니다.")
