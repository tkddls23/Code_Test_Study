#Recursive Version
def solution(x):

    if x==0:
        return 0
    
    elif x==1:
        return 1

    else:
        return solution(x-1)+solution(x-2)

#Iterative Version
def solution(x):

    answer=0
    
    r=0
    y=0
    z=0
    
    i=0
    while i<=x:
        z=r+y

        if i==1:
            y=1
            z=r+y

        else:
            r=y
            y=z
            
        i+=1
    
    answer=z
    return answer