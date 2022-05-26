def solution(L, x):
    answer = -1
    first, last = 0, len(L)-1

    while first <= last:
        mid = (first+last) // 2
        if L[mid] == x:
            answer = mid
            break
        elif L[mid] < x:
            first = mid + 1
        elif L[mid] > x:
            last = mid - 1

    return answer
