n = int(input())
for y in range(n//5, -1, -1):
    if (n-5*y) % 3 == 0:
        print(y + (n-5*y) // 3)
        break
else:
    print(-1)