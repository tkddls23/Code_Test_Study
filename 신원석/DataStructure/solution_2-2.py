def solution(L, x):
    answer = []
    while True:
        if x in L:
            answer.append(L.index(x))
            L[L.index(x)] = x+1
        elif len(answer) == 0:
            answer.append(-1)
            break
        else:
            break
    return answer
