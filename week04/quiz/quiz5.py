coin500 = int(input("500원짜리 개수 --> "))
coin100 = int(input("100원짜리 개수 --> "))
coin50 = int(input("50원짜리 개수 --> "))
coin10 = int(input("10원짜리 개수 --> "))

total = (coin500 * 500) + (coin100 * 100) + (coin50 * 50) + (coin10 * 10)

print("## 동전의 합계 ==> %d원" % total)
