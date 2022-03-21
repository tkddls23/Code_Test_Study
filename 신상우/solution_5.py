5

#첫 번째 시도
L = [2,3,5,6,9,11,15]
x = 6
l = 0 
u = 6

def solution(L, x, l, u):
    if l > u:
        return -1

    mid = (l + u) // 2

    if x == L[mid]:
        return mid
    elif x < L[mid]:
        u = mid - 1
        return solution(L, x, l, u)

    else:
        l = mid + 1
        return solution(L, x, l, u)

#재시도

L =  [0,3,5,6,9,11,15]
x = 0
l = 0
u = 6
def solution(L, x, l, u):
    if l > u:
        return -1

    mid = (l + u) // 2

    if x == L[mid]:
        return mid
    elif x < L[mid]:
        return solution(L[:mid], x, l, mid - 1)

    else:
        return solution(L[mid+1:], x, l, mid + 1)

print(solution(L, x, l, u))

#재시도2
#u에는 mid - 1
#l에는 mid + 1 을 넣어줘야 함

def solution(L, x, l, u):
    if l > u:
        return -1

    mid = (l + u) // 2

    if x == L[mid]:
        return mid
    elif x < L[mid]:
        return solution(L, x, l, mid - 1)

    else:
        return solution(L, x, mid + 1, u)

