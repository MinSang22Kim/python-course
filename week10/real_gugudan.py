print("==========================================")
print("|             구구단 프로그램            |")
print("==========================================\n")

for k in [2, 5, 8]:
    # 제목 출력
    print("==========================================")
    for j in range(k, k + 3):
        if j <= 9:
            print(f"|    {j}단     |", end="")
    print("")
    print("==========================================")

    # 구구단 본문 출력
    for i in range(1, 10):
        for j in range(k, k + 3):
            if j <= 9:
                print("| %d * %d = %2d |" % (j, i, j*i), end="")
        print("")
    print()