# 0부터 2까지 1씩 증가하면 출력(0, 1, 2가 줄바꿈되어 출력)
for i in range(0, 3, 1):
    print(i)
print()

# 증가값이 커도 처음에 한번은 무조건 출력됨(0이 출력)
for i in range(0, 3, 999):
    print(i)
print()

# hap 변수 초기화 필요
hap = 0
for i in range(2, 10, 1):
    hap = hap + i
print(hap)
