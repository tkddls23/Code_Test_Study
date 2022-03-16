'''
L을 순회하며, x가 어떤 value의 이하인 순간
value의 인덱스에 x를 삽입

그 외엔 x가 L의 최댓값인 경우이므로 L의 끝에 삽입
'''
def solution(L, x):
    for i in range(len(L)):
        if x <= L[i]:
            L.insert(i, x)
            break

    if x > L[-1]:
        L.append(x)
    
    return L


'''
L에 x를 삽입한 후 정렬
'''
def solution(L, x):
    L.append(x)
    L.sort()
    return L