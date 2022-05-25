# 검증수
num = input().split()
num = list(map(int,num))
num = [num[i]**2 for i in range(len(num))]
print(sum(num)%10)