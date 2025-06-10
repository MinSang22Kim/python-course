ss = "IT_CookBook"

result1 = '#'.join(ss)
print(result1) # 출력: I#T#_#C#o#o#k#B#o#o#k

result2 = ss.join('#')
print(result2) # 출력: #

result3 = ss.split('#')
print(result3) # 출력: ['IT_CookBook']

result4 = '#'.split(ss)
print(result4) # 출력: ['#']
