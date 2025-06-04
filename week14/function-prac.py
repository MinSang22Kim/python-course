# *para는 가변인자, 인자 개수가 정해져 있지 않은 경우 사용
# 여러 개의 인자를 튜플로 받아서 처리 가능 
def multi(*para):
    result = 0
    for num in para:
        result += num
    return result

hap = multi(1, 2, 3)
print("멀티함수에서 리턴된 값 => %d" % hap)
