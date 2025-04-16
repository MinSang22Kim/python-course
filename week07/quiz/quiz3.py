import random

a="abcdefghij"
b="0123456789"

passw=random.choice(a+b)
passw=passw+random.choice(a+b)
passw=passw+random.choice(a+b)

print("생성된 패스워드: ", passw)
