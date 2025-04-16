a = [1, 2, 3, 'a', 'b']
print(a)

a.append(100)
print(a)

cafe=['coffee', 'tea', 'snack', 'food']
ans=input("검색할 상품을 입력하세요: ")

if ans in cafe:
    print("상품이 준비되어 있습니다.")
else:
    print("상품이 없습니다.")
