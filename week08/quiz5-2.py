import random

n1 = random.randint(1, 100)
n2 = random.randint(1, 100)
num=int(input("%d-%d= "% (n1, n2)))
# problem = str(n1) +"-"+ str(n2) +"="
# ans=int(input(problem))

if num==n1-n2:
    print("정답입니다.")
else:
    print("틀렸습니다.")
