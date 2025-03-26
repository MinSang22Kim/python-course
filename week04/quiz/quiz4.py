money = int(input("투입한 돈: "))
item_price = int(input("물건값: "))

change = money - item_price
coin_500 = change // 500
change %= 500
coin_100 = change // 100
change %= 100

print("=====================")
print("거스름돈:", money - item_price)
print("500원 동전의 개수:", coin_500)
print("100원 동전의 개수:", coin_100)
print("=====================")
