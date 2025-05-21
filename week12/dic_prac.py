items = {"펜": 10, "종이": 30}
item = input("재고를 확인할 상품을 입력하시오: ")

if item in items:
    print(f"{item}의 재고는 {items[item]}개입니다.")
else:
    print("해당 상품은 재고 목록에 없습니다.")
    