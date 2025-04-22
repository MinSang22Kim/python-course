money=int(input("받은 돈: "))
price=int(input("물건 값: "))

change=money-price
n500=change//500
n100=change%500//100

print("========================")
print("거스름돈: %d"%change)
print("500원 동전 개수: %d"%n500)
print("100원 동전 개수: %d"%n100)
