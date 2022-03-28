def solution(L, x, l, u):
    if l>u:
        return -1

    mid = (l + u) // 2

    if x == L[mid]:
        return mid
    
    elif x < L[mid]:
        u=mid-1
        return solution(L, x, l, u)

    else:
        l=mid+1
        return solution(L, x, l, u)
