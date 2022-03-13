#재귀적 방법

def solution(x):
    if x < 2:
        return x
    else: 
        return solution(x-1) + solution(x-2)

#반복적 방법

def solution(x):
    one = 0
    two = 1 
    if x < 2:
        return x
    else:
        for i in range(1,x):
            fibo = one + two
            one = two
            two = fibo
        return fibo
        