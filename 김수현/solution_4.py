#재귀적 방법
def solution(x):
    if x <= 1:
        answer = x
    else:
        answer = solution(x-1) + solution(x-2)
    return answer

#반복적 방법
def solution(x):
    curr, next = 0, 1
    if x == 0:
        return 0
    elif x == 1 or x == 2:
        return 1
    for i in range(x):
        curr, next = next, curr+next

    return curr