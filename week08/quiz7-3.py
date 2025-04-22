import random
alpha="abcdefghijklmnopqrstuvwxyz"
num="1234567890"
pw=""
pw+=random.choice(alpha+num)
pw+=random.choice(alpha+num)
pw+=random.choice(alpha+num)
print("생성된 패스워드: %s"%(pw))
