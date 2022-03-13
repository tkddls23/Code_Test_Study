#2-2

def solution(L, x):
    answer = []
    element = 0 
    while(x in L):
        n = L.index(72)
        element += n
        L = L[n+1:]

        answer.append(element)
        element += 1
    if answer == []:
        answer.append(-1)
    return answer

#재시도
#index(x) 대신 index(72)라고 적어 놓았다.

def solution(L, x):
    answer = []
    element = 0 
    while(x in L):
        n = L.index(x)
        element += n
        L = L[n+1:]

        answer.append(element)
        element += 1
    if answer == []:
        answer.append(-1)
    return answer
