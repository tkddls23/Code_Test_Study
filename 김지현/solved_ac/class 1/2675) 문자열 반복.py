for t in range(int(input())):
    r, S = input().split()
    for s in S:
        print(s * int(r), end='')
    print()