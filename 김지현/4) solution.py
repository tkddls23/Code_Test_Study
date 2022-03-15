def solution(x):
    if x <= 1:
        return x
    else:
        return solution(x-2) + solution(x-1)


'''
이전의 피보나치 수열 값들을 리스트에 기록하여, 다음 수열 값을 구함
'''
def solution(x):
    index = 0
    numbers = []

    while index <= x:
        if index <= 1:
            numbers.append(index)
        else:
            numbers.append(numbers[index-2] + numbers[index-1])
        
        index +=1
    
    return numbers[-1]