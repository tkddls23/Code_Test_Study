def solution(L, x, l, u):
    if l > u:
        return -1

    mid = (l + u) // 2

    if x == L[mid]:
        return mid
    elif x < L[mid]:
        return solution(L, x, l, mid-1)

    else:
        return solution(L, x, mid+1, u)

A = [2,3,5,6,9,11,15]
b = 6
c = 0
d = 6
print(solution(A,b,c,d))
O = [2,5,7,9,11]
p = 4
q = 0
r = 4
print(solution(O,p,q,r))