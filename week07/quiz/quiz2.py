rate = float(input("이자율(단위: %): "))
money = int(input("원금(단위: 원): "))
year = int(input("거치 기간(단위: 년): "))

result = money * (1 + rate) ** year

print("%d년 후의 원리금은 %.1f원입니다."%(year, result))
