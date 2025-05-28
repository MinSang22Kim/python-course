def get_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

score = int(input("성적을 입력하세요: "))
grade = get_grade(score)

print(f"학점은 {grade} 입니다.")
