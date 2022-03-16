'''
이전 두 개의 값을 더한 값인 피보나치 수열 값을 three 변수에 할당하고,
one, two 변수를 업데이트 하여 새로운 three 값을 얻어 나감
'''
def solution(x):
    if x <= 1:
        return x
    
    one, two = 0, 1
    for i in range(2, x+1):
        three = one + two
        one = two
        two = three

    return three


'''
피보나치 수열 값인 two는 기존의 one과 two를 더한 값으로 업데이트 하고,
one은 기존의 two 값으로 업데이트 하여, 다음 수열 값을 구해 나갈 수 있도록 함
'''
def solution(x):
    if x <= 1:
        return x
    
    one, two = 0, 1
    for i in range(2, x+1):
        one, two = two, one + two

    return two


'''
if-else 축약문
'''
def solution(x):
    return x if x <= 1 else solution(x-2) + solution(x-1)