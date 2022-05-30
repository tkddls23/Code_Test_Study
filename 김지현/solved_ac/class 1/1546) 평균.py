n = int(input())
scores = list(map(int, input().split()))
print((sum(scores)/max(scores)*100) / n)