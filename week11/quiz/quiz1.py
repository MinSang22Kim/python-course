aa = []

for i in range(10):
    aa.append(0)

for i in range(10):
    aa[i] = int(input(str(i + 1) + "번 숫자: "))

hap, i = 0, 0
while i < 10:
    hap += aa[i]
    i += 1

print("total=%d" % hap)
