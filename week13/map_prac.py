# 문자열 리스트를 정수 리스트로 변환
str_nums = ['1', '2', '3']
print(str_nums) # ['1', '2', '3']

int_nums = list(map(int, str_nums)) # 각 문자열 요소에 int() 적용
print(int_nums)  # [1, 2, 3]

# 문자열 리스트를 대문자로 변환
words = ['apple', 'banana', 'cherry']
upper_words = list(map(str.upper, words)) # 각 문자열에 .upper() 적용
print(upper_words)  # ['APPLE', 'BANANA', 'CHERRY']

# 숫자 리스트의 각 값 제곱
nums = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, nums))
print(squared)  # [1, 4, 9, 16]
