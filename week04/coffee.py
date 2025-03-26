coffee_p=2500
snack_p=3000
tea_p=3000

coffee=int(input("커피의 판매 개수를 입력하세요: "))
snack=int(input("스낵의 판매 개수를 입력하세요: "))
tea=int(input("차의 판매 개수를 입력하세요: "))

sales=coffee_p*coffee+snack_p*snack+tea_p*tea

print("오늘의 매출은 %d원입니다.", sales)