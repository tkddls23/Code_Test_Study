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
    match = { # 맞는 괄호 딕셔너리로 지정
        ')': '(',
        '}': '{',
        ']': '['
    }
    S = ArrayStack()
    for c in expr:
        if c in '({[':
            S.push(c) # 여는 괄호는 스택에 push

        elif c in match: # 닫는 괄호일 때
            if S.isEmpty(): # 스택이 비어있으면 False
                return False
            else:
                t = S.pop()
                if t != match[c]: # 여는괄호-닫는괄호 짝이 맞지 않으면 False
                    return False

    return S.isEmpty() # 끝까지 검사 후 스택이 비어있어야 올바른 수식!!