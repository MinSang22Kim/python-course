id="KUTIS"
pw="12345"

user_id=input("아이디를 입력하시오: ")
if(user_id==id):
    user_pw=input("비밀번호를 입력하시오: ")
    if(user_pw==pw):
        print("환영합니다!")
    else:
        print("비밀번호가 틀렸습니다.")
else:
    print("아이디가 틀렸습니다.")
    