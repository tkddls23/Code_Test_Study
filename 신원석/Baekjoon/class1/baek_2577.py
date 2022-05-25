# 숫자의 개수
multiple = 1
for i in range(3):
    num = int(input())
    multiple *= num

multiple = str(multiple)

for i in range(0,10):
    print(multiple.count(str(i)))

