#파이썬 eval() 알아보기

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


def infixToPostfix(tokenList):
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
        else: 
            if c == '(' or opStack.isEmpty():
                opStack.push(c)
            elif c in prec:
                if prec[c] > prec[opStack.peek()]: #크면 위로 올린다.
                    opStack.push(c)
                else: #작거나 같으면 빼고 넣는다
                    postfixList.append(opStack.pop())
                    opStack.push(c)
            else:
                while opStack.peek() != '(':
                    postfixList.append(opStack.pop())
                opStack.pop()
                     
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    

    return postfixList

#문자열을 풀어서 한 번에 else로 구할 수 있는 방법은 없을까?
def postfixEval(tokenList):
    valStack = ArrayStack()

    for token in tokenList:
        if type(token) is int:
            valStack.push(token)
        elif token == '*': 
            b = valStack.pop()
            a = valStack.pop()
            c = a * b
            valStack.push(c)
        elif token == '/': 
            b = valStack.pop()
            a = valStack.pop()
            c = a / b
            valStack.push(c)
        elif token == '+': 
            b = valStack.pop()
            a = valStack.pop()
            c = a + b
            valStack.push(c)
        elif token == '-': 
            b = valStack.pop()
            a = valStack.pop()
            c = a - b
            valStack.push(c)
    return valStack.pop()


def solution(expr):
    tokens = splitTokens(expr)
    postfix = infixToPostfix(tokens)
    val = postfixEval(postfix)
    return val

# S = "(12+5)*(1+1)"
# a = splitTokens(S)
# print(a)
# b = infixToPostfix(a)
# print(b)
# print(solution(S))