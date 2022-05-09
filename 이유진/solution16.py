* solution.py *

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


def splitTokens(exprStr):
    tokens = []
    val = 0
    valProcessing = False
    for c in exprStr:
        if c == ' ':
            continue
        if c in '0123456789':
            val = val * 10 + int(c)
            valProcessing = True
        else:
            if valProcessing:
                tokens.append(val)
                val = 0
            valProcessing = False
            tokens.append(c)
    if valProcessing:
        tokens.append(val)

    return tokens


def infixToPostfix(tokenList): #리스트 리턴 
    prec = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
    }

    opStack = ArrayStack()
    postfixList = []
    
    for c in tokenList:
        if type(c) is int:
            postfixList.append(c)
        
        elif c=='(':
            opStack.push(c)
        
        elif c==')':
            while not opStack.peek()=='(':
                postfixList.append(opStack.pop())
            opStack.pop()
        
        else:
            if opStack.isEmpty():
                opStack.push(c)
                
            else:
                while opStack.isEmpty()==False and prec[c] <= prec[opStack.peek()]:
                    postfixList.append(opStack.pop())
                opStack.push(c)
                
    
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())

    return postfixList


def postfixEval(tokenList): #연산
    
    opStack = ArrayStack()
    
    for j in tokenList:
        if type(j) is int: #피연산자는 push
            opStack.push(j)
            
        #연산자는 앞에 두 개 pop, 계산하고 push 
        elif j == '+':
            num2=opStack.pop()
            num1=opStack.pop()
            opStack.push(num1+num2)
        
        elif j == '-':
            num2=opStack.pop()
            num1=opStack.pop()
            opStack.push(num1-num2)
            
            
        elif j == '*':
            num2=opStack.pop()
            num1=opStack.pop()
            opStack.push(num1*num2)
            
            
        else:
            num2=opStack.pop()
            num1=opStack.pop()
            opStack.push(num1/num2)
            
            
    #마지막 원소일 때 pop 
    answer=opStack.pop()    
    
    return answer
    
    


def solution(expr):
    tokens = splitTokens(expr)
    postfix = infixToPostfix(tokens)
    val = postfixEval(postfix)
    return val