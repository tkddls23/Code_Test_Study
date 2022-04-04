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

    for i in tokenList:

        if i in prec:
            if opStack.isEmpty() or i == '(':
                pass
            elif prec[opStack.peek()] < prec[i]:
                pass
            else:
                while not opStack.isEmpty() and prec[opStack.peek()] >= prec[i]:
                    postfixList.append(opStack.pop())
            opStack.push(i)

        else:
            if i == ')':
                while opStack.peek() != '(':
                    postfixList.append(opStack.pop())
                opStack.pop()
            else:
                postfixList.append(i)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return postfixList


def postfixEval(tokenList):
    valstack = ArrayStack()
    val = 0
    for tk in tokenList:
        if type(tk) is int:
            valstack.push(tk)
        else:  # 연산자인 경우
            opr2 = valstack.pop()
            opr1 = valstack.pop()
            if tk == '+':
                val = opr1+opr2
            elif tk == '-':
                val = opr1-opr2
            elif tk == '*':
                val = opr1*opr2
            elif tk == '/':
                val = opr1/opr2
            valstack.push(val)
            val = 0
    val = valstack.pop()
    return val


def solution(expr):
    tokens = splitTokens(expr)
    postfix = infixToPostfix(tokens)
    val = postfixEval(postfix)
    return val
