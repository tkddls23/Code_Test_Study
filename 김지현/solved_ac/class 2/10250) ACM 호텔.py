for t in range(int(input())):
    H, W, N = map(int, input().split())

    if N % H == 0:
        floor = H
        num = N // H
    else:
        floor = N % H
        num = N // H + 1

    print(floor*100 + num)