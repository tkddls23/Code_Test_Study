# 문자열 반복
repeat = []
string = []
num = int(input())
for i in range(num):
    test = input().split()
    repeat.append(int(test[0]))
    string.append(test[1])

for j in range(num):
    a = [repeat[j]*i for i in string[j]]
    for p in a:
        print(p, end='')
    print('')