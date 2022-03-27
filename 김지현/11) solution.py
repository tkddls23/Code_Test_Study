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


# 괄호 유효성 검사
def solution(expr):
    match = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    S = ArrayStack()
    for c in expr:
        if c in '({[':
            S.push(c)

        elif c in match:
            if S.isEmpty(): # 여는 괄호가 없는 경우
                return False
            else:
                t = S.pop()
                if t != match.get(c): # 여는 괄호와 쌍이 안 맞는 경우
                    return False
    return S.isEmpty() # 더 이상 여는 괄호가 안 남아 있는지 검사


print(solution("[(A + B) * C]")) # True
print(solution("{(A + B} * C)")) # False