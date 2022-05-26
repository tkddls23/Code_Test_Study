'''
인자로 주어진 문자열 expr 은 소괄호와 사칙연산 기호, 그리고 정수들로만 이루어진 중위 표현 수식이다.

함수 solution() 은 이 수식의 값을 계산하여 그 결과를 리턴한다.
이를 위한 infixToPostfix(), postfixEval() 함수를 구현하라.
'''
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


def splitTokens(exprStr): # 문자열 형태의 수식을 각 자료형에 맞게 바꿔서 리스트 형태로 변환해주는 함수
    tokens = []
    val = 0
    valProcessing = False
    for c in exprStr:
        if c == ' ':
            continue
        if c in '0123456789':
            val = val * 10 + int(c)
            valProcessing = True
        else: # 연산자
            if valProcessing:
                tokens.append(val)
                val = 0
            valProcessing = False
            tokens.append(c) # 연산자는 그대로 리스트에 추가
    if valProcessing:
        tokens.append(val)

    return tokens


def infixToPostfix(tokenList): # 중위 표기 수식(리스트)를 후위 표기 수식(리스트)로 변환하는 함수
    prec = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
    }

    opStack = ArrayStack()
    postfixList = []

    for token in tokenList:
        if type(token) is int: # 피연산자 (정수)
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            while True:
                t = opStack.pop()
                if t == '(':
                    break
                postfixList.append(t)
        else: # 사칙연산자
            while not opStack.isEmpty() and prec[token] <= prec[opStack.peek()]:
                t = opStack.pop()
                postfixList.append(t)
            opStack.push(token)

    while not opStack.isEmpty():
        t = opStack.pop()
        postfixList.append(t)

    return postfixList


def postfixEval(tokenList): # 후위 표기 수식을 계산하는 함수
    valStack = ArrayStack()

    for token in tokenList:
        if type(token) is int: # 피연산자
            valStack.push(token)
        else: # 연산자
            rightVal = valStack.pop()
            leftVal = valStack.pop()
            if token == '+':
                val = leftVal + rightVal
            elif token == '-':
                val = leftVal - rightVal
            elif token == '*':
                val = leftVal * rightVal
            elif token == '/':
                val = leftVal / rightVal
            valStack.push(val) # 계산 결과를 push

    return valStack.pop() # 마지막에 Stack에는 계산 결과값만 남아있음


def solution(expr):
    tokens = splitTokens(expr) # 중위 표기 수식(문자열)을 리스트 형태로 변환
    postfix = infixToPostfix(tokens) # 중위 표기 수식(리스트)를 후위 표기 수식(리스트)로 변환
    val = postfixEval(postfix) # 후위 표기 수식을 계산한 결과 반환
    return val


# 예시 "12 * (9 - (3+2))" -> [12, '*', '(', 9, '-', '(', 3, '+', 2, ')', ')'] -> [12, 9, 3, 2, '+', '-', '*'] -> 48
expr = "12 * (9 - (3+2))"
print("계산 결과:", solution(expr))
