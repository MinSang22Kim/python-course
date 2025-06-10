ss = "python test STRING"

print("1) title():", ss.title())        # 각 단어 첫 글자 대문자
print("2) upper():", ss.upper())        # 모두 대문자
print("3) swapcase():", ss.swapcase())  # 대소문자 바꿔치기
print("4) lower():", ss.lower())        # 모두 소문자


s = "Python"
for ch in s:
    print(ch, end='-')

s = "Python"
print(s[::-1])

new_str = ""
 # 5 → 0, end값은 0이하로 작아져도(ex. -1, -5) 결과는 같음
for i in range(len(s)-1, 0, -1):
    new_str += s[i]
