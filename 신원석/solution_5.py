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

# 이진탐색
'''
중간부터 탐색 시작 
찾으려는 원소(x)가 mid에 위치한 값과 같으면 mid return
mid에 위치값보다 작으면 last인덱스값(u)를 mid-1로 설정하고 다시 solution() 실행
mid에 위치값보다 크면 first인텍스값(l)를 mid+1로 설정하고 다시 solution() 실행
'''