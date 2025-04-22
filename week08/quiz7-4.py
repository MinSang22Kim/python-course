age = int(input("강아지 나이 입력(음수 안됨): "))

if age <= 2:
    human_age = age * 10
else:
    human_age=2*10+(age-2)*4

print("강아지 나이를 사람 나이로 환산하면 %d살입니다."%human_age)