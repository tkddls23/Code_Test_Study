'''
소괄호: ( ), 중괄호: { }, 대괄호: [ ]를 포함할 수 있는
수식을 표현한 문자열 expr 이 인자로 주어질 때,
이 수식의 괄호가 올바르게 여닫혀 있는지를 판단하는 함수 solution() 을 완성하세요. 
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


def solution(expr):
    match = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    S = ArrayStack()
    for c in expr:
        if c in '({[': # 여는 괄호이면
            S.push(c)

        elif c in match: # 닫는 괄호이면
            if S.isEmpty():
                return False
            else:
                t = S.pop()
                if t != match[c]: # 쌍이 맞지 않으면
                    return False
    return S.isEmpty() # 다 읽은 후 스택이 비어있어야 True


L = ArrayStack()
expr = "{(A + B} * C)"
print(solution(expr))
