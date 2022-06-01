N, target = map(int, input().split())
arr = list(map(int, input().split()))
result = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            sum = arr[i] + arr[j] + arr[k]
            if sum > target:
                continue
            else:
                result  = max(result, sum)

print(result)