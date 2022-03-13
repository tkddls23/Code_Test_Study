#3

def solution(L, x):
    left = 0
    right = len(L) - 1

    while left <= right:
        mid = (left + right) // 2
        
        if L[mid] == x:
            return mid
        elif L[mid] > x: 
            right = mid - 1
        else:
            left = mid + 1
        
    return -1