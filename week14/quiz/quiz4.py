def f1():
    print(var)

def f2():
    var = 10
    print(var)

var = 100
f1()  # 🔹 출력: 100 (전역 변수 사용)
f2()  # 🔹 출력: 10 (지역 변수 사용)
