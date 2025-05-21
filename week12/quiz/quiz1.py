items = {
    "펜": 10,
    "종이": 20,
    "우유": 30,
    "종이컵": 40,
    "책": 50,
    "커피": 60,
    "음료": 70,
    "콜라": 80
}

print("╔════════════════════════════╗")
print("║     재고 관리 프로그램     ║")
print("╚════════════════════════════╝")

while True:
    print()
    print("╔════════ 메뉴 선택 ═════════╗")
    print("║ 0: 종료                    ║")
    print("║ 1: 재고 추가               ║")
    print("║ 2: 재고 감소               ║")
    print("║ 3: 재고 확인               ║")
    print("╚════════════════════════════╝")
    print()

    num = int(input("무엇을 하시겠습니까? (번호 입력): "))
    print()

    if num == 1:
        item = input("추가할 상품명을 입력하세요: ")
        amount = int(input("추가할 수량을 입력하세요: "))
        if item in items:
            items[item] += amount
        else:
            items[item] = amount
        print(f"{item}의 재고가 {amount}개 추가되었습니다.")
        print(f"{item}의 현재 재고: {items[item]}개")

    elif num == 2:
        item = input("감소시킬 상품명을 입력하세요: ")
        if item in items:
            amount = int(input("감소시킬 수량을 입력하세요: "))
            print()
            if amount <= items[item]:
                items[item] -= amount
                print(f"{item}의 재고가 {amount}개 감소되었습니다.")
                print(f"남은 재고: {items[item]}개")
            else:
                print("감소할 수량이 현재 재고보다 많습니다.")
        else:
            print("해당 상품은 재고 목록에 없습니다.")

    elif num == 3:
        print("#### 재고 목록 ####")
        print("%5s %8s" % ("상품명", "재고수량"))
        print("-" * 20)
        for key in items:
            print("%5s %9d개" % (key, items[key]))

    elif num == 0:
        print("프로그램을 종료합니다.")
        break

    else:
        print("잘못된 번호입니다. 0~3 중에서 선택해주세요.")
