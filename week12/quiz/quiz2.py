dictionary = {
    "one": "하나",
    "two": "둘",
    "three": "셋",
    "four": "넷",
    "five": "다섯",
    "six": "여섯",
    "seven": "일곱",
    "eight": "여덟",
    "nine": "아홉",
    "ten": "열"
}

print("╔═══════════════════════════╗")
print("║     영한사전 프로그램     ║")
print("╚═══════════════════════════╝")

while True:
    print()
    print("╔════════ 메뉴 선택 ════════╗")
    print("║ 0: 종료                   ║")
    print("║ 1: 단어 추가              ║")
    print("║ 2: 단어 삭제              ║")
    print("║ 3: 단어 검색              ║")
    print("╚═══════════════════════════╝")
    print()

    num = int(input("원하는 작업을 선택하세요: "))
    print()

    if num == 0:
        print("프로그램을 종료합니다.")
        break

    elif num == 1:
        eng = input("추가할 영어 단어를 입력하세요: ")
        kor = input(f"'{eng}'의 뜻을 입력하세요: ")
        dictionary[eng] = kor
        print(f"단어 '{eng}'이(가) 추가되었습니다.")

    elif num == 2:
        eng = input("삭제할 영어 단어를 입력하세요: ")
        if eng in dictionary:
            del dictionary[eng]
            print(f"단어 '{eng}'이(가) 삭제되었습니다.")
        else:
            print("해당 단어는 사전에 없습니다.")

    elif num == 3:
        word = input("검색할 영어 단어를 입력하세요: ")
        if word in dictionary:
            print(f"{word}의 뜻은 '{dictionary[word]}'입니다.")
        else:
            print("해당 단어는 사전에 없습니다.")

    else:
        print("올바른 번호를 선택해주세요.")
        