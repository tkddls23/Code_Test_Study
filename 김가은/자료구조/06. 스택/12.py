# 중위 표기법을 따르는 수식을 후위 표기법을 따르는 수식으로 변환하여 반환하는 함수 solution() 을 완성하세요.
# 수식은 항상 유효하다고 가정
# 수식의 구성은 알파벳 A~Z, 사칙연산자 + - * /, 괄호 ( ) 로 이루어짐  [공백 문자는 포함되지 않음]

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

def solution(exp):
    opStack = ArrayStack()
    ret = ''

    for c in exp: # 수식 한 글자씩 확인
        if c >= 'A' and c <= 'Z': # 피연산자
            ret += c
        else: # 연산자
            if c == '(':
                opStack.push(c)
            elif c == ')':
                while True:
                    t = opStack.pop()
                    if t == '(':
                        break
                    ret += t
            else: # 사칙연산자
				# 스택에 쌓여있는 연산자와 1:1로 차례대로 비교 -> 맞는 위치를 찾음
                while not opStack.isEmpty() and prec[c] <= prec[opStack.peek()]: # *** 스택이 비어있으면 비교할 연산자X -> 비어있는지 반드시 확인 필요
                    t = opStack.pop()
                    ret += t
                opStack.push(c)

    # 수식을 다 훑은 뒤 스택에 남아있는 연산자 전부 꺼내기
    while not opStack.isEmpty():
        t = opStack.pop()
        ret += t

    return ret


exp = "A*(B+C)"
convertExp = solution(exp)
print(convertExp)