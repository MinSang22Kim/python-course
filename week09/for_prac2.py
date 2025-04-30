# end=''로 줄바꿈 없이 출력
for i in [0, 1, 2]:
    print("test", end='')

i = hap = 0
for i in range(1, 11, 1):
    hap += i
print("최종합: %d"%hap)

hap=0
num = int(input("값을 입력하시오: "))
for i in range(1, num+1, 1):
    hap = hap + i
print("최종합: %d"%hap)
