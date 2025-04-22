rate=int(input("이자율(단위: %): "))
price=int(input("원금(단위: 만원): "))
year=int(input("거치기간(단위: 년): "))

print("%d년 후의 원리금은 %f원입니다."%(year, (price*(1+rate/100)**year)))
