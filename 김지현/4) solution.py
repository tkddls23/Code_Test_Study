def solution(x):
    if x <= 1:
        return x
    else:
        return solution(x-2) + solution(x-1)



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