'''
L을 순회하며, value가 x와 일치할 때의 index 값들을 새로운 리스트에 삽입
'''
def solution(L, x):
    if x not in L:
        return [-1]

    answer = []
    for i in range(len(L)):
        if L[i] == x:
            answer.append(i)

    return answer


'''
L에서 x와 일치하는 value의 첫번째 index 값을 새로운 리스트에 삽입 후,
L의 그 다음 index부터 새롭게 찾아진 x의 index 값을 얻는 과정을 while문을 통해 실행
'''
def solution(L, x):
    if x not in L:
        return [-1]

    answer = []
    index = L.index(x)

    try:
        while True:
            answer.append(index)
            index = L.index(x, index + 1)

    except ValueError: # L에 더이상 x가 없을 때, 시작 index > 리스트의 길이가 될 때 
        return answer