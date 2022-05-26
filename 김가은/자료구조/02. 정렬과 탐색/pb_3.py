# 리스트가 정렬되어 있고 중복된 원소는 없다고 가정한다.
# 리스트 L에서 x를 찾는 이진 탐색 함수를 구현하시오.
# x를 찾으면 index를 반환. x가 리스트에 없으면 -1을 반환.

def solution(L, x):
    lower = 0
    upper = len(L) - 1
    idx = -1

    while lower <= upper:
        middle = (lower + upper) // 2
        if L[middle] == x:
            idx = middle
            break
        elif L[middle] < x:
            lower = middle + 1
        else:
            upper = middle - 1
            
    return idx

# L = []
# x = 3
# print(solution(L, x))