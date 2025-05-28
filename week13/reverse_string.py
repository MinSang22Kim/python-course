instr, outstr = "", ""
i, count = 0, 0

instr = input("문자열을 입력하세요: ")
count = len(instr)

for i in range(0, count):
    outstr = outstr + instr[count - (i+1)]

print("반대로 출력된 문자열 -->%", outstr)
