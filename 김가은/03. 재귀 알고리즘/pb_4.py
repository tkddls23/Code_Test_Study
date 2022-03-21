# 피보나치 순열 함수 구현
# 인자로 0 또는 양의 정수인 x 가 주어짐

# 재귀적 풀이
def solution(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return solution(x-1) + solution(x-2)

# 비재귀적 풀이
def solution(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1

    one = 0
    two = 1
    for i in range(2, x+1):
        three = one + two
        one = two
        two = three
    return three

# x = 2
# print(solution(x))