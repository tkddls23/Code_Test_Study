# 평균 조작
N = int(input())
score = input().split()
score = list(map(int,score)) #list 원소 str -> int
max_score = max(score)

result = sum(score)/max_score*100/N
print(result)