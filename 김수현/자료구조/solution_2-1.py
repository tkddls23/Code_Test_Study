def solution(L, x):

    if x < min(L):
        L.insert(0, x)
    elif x > max(L):
        L.append(x)
    else:
        for i in range(len(L)-2):
            if L[i] <= x <= L[i+1]:
                index = i+1
                L.insert(index, x)

    answer = L
    return answer