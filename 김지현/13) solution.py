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


def infixToPostfix(tokenList): # 중위 -> 후위 표현식
    prec = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
    }

    opStack = ArrayStack()
    postfixList = []

    for t in tokenList:
        if type(t) is int:
            postfixList.append(t)

        elif t == "(":
            opStack.push(t)

        elif t == ")":
            while opStack.peek() != "(":
                postfixList.append(opStack.pop())
            opStack.pop()
        
        else:
            while opStack.size() and prec[t] <= prec[opStack.peek()]:
                postfixList.append(opStack.pop())
            opStack.push(t)
    
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())

    return postfixList


def postfixEval(tokenList): # 후위 표현식 계산
    opStack = ArrayStack()

    for t in tokenList:
        if type(t) is int:
            opStack.push(t)

        else:
            forth, back = opStack.pop(), opStack.pop()

            if t == "+":
                opStack.push(back+forth)
            elif t == '-':
                opStack.push(back-forth)
            elif t == '*':
                opStack.push(back*forth)
            else:
                opStack.push(back/forth)

    return opStack.pop()


def solution(expr):
    tokens = splitTokens(expr)
    postfix = infixToPostfix(tokens)
    val = postfixEval(postfix)
    return val


print(solution("5+3")) # 8
print(solution("(1 + 2) * (3 + 4)")) # 21
print(solution("7 * (9 - (3+2))")) # 28