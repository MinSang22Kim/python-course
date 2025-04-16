import random

a="abcdefghij"
b="0123456789"

passw=random.choice(a+b)
passw=passw+random.choice(a+b)
passw=passw+random.choice(a+b)

print("임시 비밀번호: ", passw)
