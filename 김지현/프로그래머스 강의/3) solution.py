'''
탐색 범위의 최댓값 - 최솟값 > 1인 경우: L에서 x와 일치하는 value의 위치에 따라,
최댓값 or 최솟값을 중간값으로 설정하여, x의 탐색 범위를 좁게 설정

최댓값 - 최솟값 = 1인 경우: x가 그 범위의 최댓값이거나 최솟값임
'''
def solution(L, x):
    lower = 0
    upper = len(L) - 1
    index = -1

    while upper - lower > 1:
        middle = (lower + upper) // 2
        
        if L[middle] == x:
            index = middle
            return index
        elif L[middle] < x:
            lower = middle
        else:
            upper = middle

    if upper - lower == 1:
        if L[upper] == x:
            index = upper
        elif L[lower] == x:
            index = lower

    return index