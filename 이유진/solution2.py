#1
def solution(L, x):
    answer = []
    
    answer=L
    a=-1
    
    for num in answer:
        if num>x:  
            a=answer.index(num)
            answer.insert(a,x)
            break

    if a==-1:
        answer.append(x)

    return answer

    #2
    def solution(L, x):
    answer = []
    
    answer=L
    num=[]
    i=0
    
    for num2 in answer:
        if x == num2:
            num.append(i)
        i+=1
            
    if len(num)==0:
        num.append(-1)
        
    answer=num
    
    return answer