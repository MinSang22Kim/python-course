age = int(input("강아지의 나이를 입력하시오:(음수 안됨) "))
if age <= 2:
    human_age = age * 10
else:
    human_age = 2 * 10 + (age - 2) * 4

print("강아지의 나이를 사람 나이로 환산하면 %d살 입니다." % human_age)
