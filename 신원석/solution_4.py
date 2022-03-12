# 재귀적 방법 O(2^n)
def solution(x):
    return x if x < 2 else solution(x-1) + solution(x-2)

# 반복적 방법 O(n)


def solution(x):
    Fs, Fe = 0, 1

    for i in range(x):

        Fs, Fe = Fe, Fs+Fe

    return Fs

# 메모이제이션 O(n)


def solution(x):

    memo = [0 for i in range(x+1)]

    if x < 2:
        return x
    else:
        if memo[x] > 0:
            return memo[x]
        else:
            memo[x] = solution(x-1) + solution(x-2)
            return memo[x]
