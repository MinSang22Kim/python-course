ss = "오늘 수업은 python입니다."

# (1) 문자열을 공백 기준으로 나눠 리스트로 만들기
words = ss.split()
print(words)  # ['오늘', '수업은', 'python입니다.']

# (2) 리스트를 '-'로 이어붙이기
joined = "-".join(words)
print(joined)  # '오늘-수업은-python입니다.'

# (3) 문자열의 양쪽 공백 제거 (strip 연습)
trimmed = ss.strip()
print(trimmed)  # '오늘 수업은 python입니다.' (여기선 공백이 없지만 연습용)

# (4) 특정 부분 문자열 바꾸기
replaced = ss.replace("python입니다.", "짱입니다.")
print(replaced)  # '오늘 수업은 짱입니다.'