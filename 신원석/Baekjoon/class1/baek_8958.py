# OX 퀴즈
num = int(input()) # case num
test= [] # test case

for i in range(num):
    test.append(input())

for i in range(num):
    correct = test[i].split('X') # X를 기준으로 분리
    correct = [i for i in correct if i]
    score = 0

    for j in correct:
        tmp = j.count('O') # 분리된 O리스트에서 O의 개수
        score += int((tmp+1)* tmp / 2)

    print(score)