price, c500, c100 = 0, 0, 0

price = int(input("금액을 입력하세요: "))

c500=price//500
price=price%500

c100=price//100
price=price%100

print("500원 = ", c500)
print("100원 = ", c100)
print("잔돈: ", price)
