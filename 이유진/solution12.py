class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}

def solution(S):
    opStack = ArrayStack()
    answer = ''
    
    for c in S:
        if c.isalpha():
            answer+=c
        
        elif c=='(':
            opStack.push(c)
        
        elif c==')':
            while not opStack.peek()=='(':
                answer+=opStack.pop()
            opStack.pop()
        
        else:
            if opStack.isEmpty():
                opStack.push(c)
                
            else:
                while opStack.isEmpty()==False and prec[c] <= prec[opStack.peek()]:
                    answer+=opStack.pop()
                opStack.push(c)
                
    
    while not opStack.isEmpty():
        answer+=opStack.pop()
    
    return answer
