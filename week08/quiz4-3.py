num=int(input("수 입력(1~3자리): "))

res=num//100
num%=100
res+=num//10
res+=num%10
print(res)
