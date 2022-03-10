def solution(L, x):
    if x not in L:
        return [-1]

    answer = []
    for i in range(len(L)):
        if L[i] == x:
            answer.append(i)

    return answer



def solution(L, x):
    if x not in L:
        return [-1]

    answer = []
    index = L.index(x)

    try:
        while True:
            answer.append(index)
            index = L.index(x, index + 1)

    except ValueError:
        return answer