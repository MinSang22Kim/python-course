num = int(input("정수(1~3자리)를 입력하세요: "))

hundreds = num // 100
tens = (num % 100) // 10
ones = num % 10

digit_sum = hundreds + tens + ones

print("자릿수의 합:", digit_sum)
