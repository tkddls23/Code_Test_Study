# x보다 작은 수

num = list(map(int, input().split()))
N = num[0]
X = num[1]

A = list(map(int, input().split()))

for i in A :
    if i < X:
        print(i, end=' ')
