'''
index와 value를 함께 리턴하는 enumerate를 사용하여,
value가 x와 일치할 때의 index 값들을 새로운 리스트에 삽입
'''
def solution(L, x):
    answer = [index for index, value in enumerate(L) if value == x]
    if not answer:
        answer.append(-1)
    
    return answer


'''
L에서 x와 일치하는 value의 index 값을 새로운 리스트에 삽입하고,
슬라이싱된, 그 다음 index부터의 L을 새로운 L로 설정하여
L에서 x의 index 값들을 얻는 과정을 while문을 통해 실행
'''
def solution(L, x): 
    answer = []
    element = 0

    while x in L:
        index = L.index(x)
        element += index
        answer.append(element)

        L = L[index+1:] # IndexError 발생 X
        element += 1

    if not answer:
        answer.append(-1)

    return answer


'''
L에서 x와 일치하는 value의 index 값을 새로운 리스트에 삽입한 후,
해당 value를 x와 다른 값으로 바꿈으로써
while문이 x의 다른 index 값들을 찾을 수 있도록 함
'''
def solution(L, x):
    answer = []
    while x in L:
        answer.append(L.index(x))
        L[L.index(x)] = x+1

    if not answer:
        answer.append(-1)
    
    return answer