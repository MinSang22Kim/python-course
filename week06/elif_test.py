## 글자 한개를 입력 - 2, 8, 10, 16 진수인지 체크해보는 것

num=input("글자 한개 입력: ")

if('0'<=num and num<= '1'):
    print("2진수 또는 8진수 또는 10진수 또는 16진수입니다.")
elif('2'<=num and num<='7'):
    print("8진수 또는 10진수 또는 16진수입니다.")
elif('8'<=num and num<='9'):
    print("10진수 또는 16진수입니다.")
elif('a'<=num and num<='f') or ('A'<=num and num<='F'): #아스키 코드값은 다르지만 소문자a든 대문자A든 16진수의 표현이다.
    print("16진수입니다.")
else:
    print("숫자가 아닙니다.")
    