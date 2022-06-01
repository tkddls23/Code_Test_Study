n = int(input())

pcs = 1
cnt = 1
while n > pcs:
    pcs += cnt*6
    cnt += 1

print(cnt)