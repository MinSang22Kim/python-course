input_str = input("문자열을 입력하세요: ")
output_str = ""

for ch in input_str:
    if ('가' <= ch <= '힣') or ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
        output_str += ch

print("한글/영문자만 남김 -->", output_str)
