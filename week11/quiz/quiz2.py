nums = []
average = 0.0

for i in range(0, 5):
    num = int(input("정수를 입력하시오: "))
    nums.append(num)
    average += num

average /= len(nums)

print("평균은 %.1f입니다." % average)
