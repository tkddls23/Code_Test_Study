def solution(L, x):
    answer = []
    #enumerate는 value와 index를 같이 반환하는 파이썬 내장 함수
    answer = [index for index, value in enumerate(L) if value == x]
    
    if not answer:
        answer.append(-1)

    return answer