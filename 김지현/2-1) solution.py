'''
1) x가 L의 최솟값일 경우: L의 0번 인덱스에 x를 삽입
2) 최댓값일 경우: L의 끝에 삽입
3) 중간에 있는 값일 경우: L[i] <= x <= L[i+1]일 때 i+1번 인덱스에 삽입
'''
def solution(L, x):
    if x < L[0]: # min(L)로도 가능
        L.insert(0, x)

    elif x > L[-1]: # max(L)로도 가능
        L.append(x)

    else:
        for i in range(len(L) - 1):
            if L[i] <= x <= L[i+1]:
                L.insert(i+1, x)
                break

    return L