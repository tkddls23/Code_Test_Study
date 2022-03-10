# len(L) >=2 라는 전제가 깔린 문제인지?

def solution(L, x):
    if x <= L[0]: # min(L)로도 가능
        L.insert(0, x)

    elif x > L[-1]: # max(L)로도 가능
        L.append(x)

    else:
        for i in range(1, len(L) - 1):
            if L[i] <= x <= L[i+1]:
                L.insert(i+1, x)
                break

    return L