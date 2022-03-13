#2-1

def solution(L, x):
    while(L[0]<=x<=L[-1]):
        for i in range(len(L)):
            if L[i] <= x and L[i+1] >= x:
                L.insert(i+1,x)
                break
        answer = L
        return answer

    return -1

#재시도: 첫 시도에서 *주의* 부분을 잘못 이해함
# 값이 범위 보다 크거나 작으면 -1을 리턴하게 코드를 짰음

def solution(L, x):
    for i in range(len(L)):
        if L[i] > x:
            L.insert(i,x)
            break
        elif L[i] <= x and L[i+1] >= x: # 같은 값이 있을 때 # 한 곳만 등호를 줘도 상관없음
            L.insert(i+1,x)
            break
        else:
            L.insert(len(L),x)
            break

    answer = L
    return answer