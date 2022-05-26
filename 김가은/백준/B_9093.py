# 백준 9093번

a = [list(map(str, input().split())) for _ in range(int(input()))]

for line in a:
    for w in line:
        print(w[::-1], end=' ')
    print()