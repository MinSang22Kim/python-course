## a, b, c, d = 0, 0, 0, 0
## sum = 0

aa=[]
for i in range(0, 4):
    aa.append(0)
hap=0

for i in range(0, 4):
    aa[i] = int(input(str(i+1)+"번 숫자: "))
    hap+=aa[i]

print("total=%d"%hap)
