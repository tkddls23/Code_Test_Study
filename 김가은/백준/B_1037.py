# 백준 1037번 - 약수

rDivsCount = int(input())
realDivs = list(map(int, input().split()))

print(min(realDivs) * max(realDivs))