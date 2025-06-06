def func1(v1, v2):
    def func2(num1, num2):
        return num1 + num2
    return func2(v1, v2)

print(func1(100, 200))  # ✅ 정상 작동
# print(func2(100, 200))  # ❌ 오류 발생
# func2는 func1 안에서 정의된 지역 함수이므로, 바깥에서는 접근 불가능함
