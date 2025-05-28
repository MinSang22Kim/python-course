str1 = 'Hanbit'
str2 = 'Network'

print("1)", str1 + str2)     # 'HanbitNetwork'
print("2)", 2 * str1)        # 'HanbitHanbit'

# 아래는 에러 확인용
try:
    print("3)", str1 * str2) # 오류
except Exception as e:
    print("3) 오류:", e)

try:
    print("4)", str1 / str2) # 오류
except Exception as e:
    print("4) 오류:", e)

try:
    print("5)", str1 - str2) # 오류
except Exception as e:
    print("5) 오류:", e)
    