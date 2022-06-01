n, c = int(input()), 1

while c < n:
    nums = map(int, list(str(c)))
    if c + sum(nums) == n:
        print(c)
        break
    c += 1

if c == n:
    print(0)