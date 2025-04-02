import random

x=random.randint(1,10)
y=random.randint(1,10)

s=str(x)+"+"+str(y)+"="
ans=int(input(s))

print(ans==x+y)
