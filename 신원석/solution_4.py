# 재귀적 방법
def solution(x):
    return x if x < 2 else solution(x-1) + solution(x-2)

# 반복적 방법


def solution(x):
    Fs, Fe = 0, 1

    for i in range(x):

        Fs, Fe = Fe, Fs+Fe

    return Fs
