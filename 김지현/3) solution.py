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