# 문제 11

# 문제만 듣고 구현 전 생각

# 스택은 함수의 호출에서 사용한다. 함수가 호출된 후 정확하게 어디로 돌아가야할지 를 알아야하기 때문
# return값을 스택에 저장한다. 
# 함수의 호출이 끝난 후 스택의 top이 가라키고 있는 곳으로만 돌아가면 되기 때문에 함수의 호출을 매우 간단하게 구현할 수 있다. 

# '('괄호를 만나고 ')' 괄호를 만나야하는 것도 스택의 특성을 이용해서 구현할 수 있다.
# '(' 함수는 return값으로 스택에 ')'을 저장하고 ')'괄호를 만났을 때 둘이 일치하는지를 확인하면 되지 않을까?

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
        if c in '({[':
            S.push(c)

        elif c in match:
            if S.isEmpty():
                return False
            else:
                t = S.pop()
                if t != match[c]:
                    return False

    return S.isEmpty()

#어떻게 풀었는지?
# - 어떻게 이런 정답을 생각했는지, 어떤 생각에서 막혔는지, 다음에는 어떻게 풀 수 있는지?, 더 좋은 방법은 없을까?
# 괄호의 유효성을 검사하기 위해서는 
# 여는 괄호와 닫는 괄호가 일치하는지, 여는 괄호가 있는지, 맨 마지막에 스택이 비어있는지(닫는 괄호가 있는지) 확인을 해야했다.
# 총 3개의 조건식이 필요하다 생각을 했는데 c를 S에 push하는 조건식을 제외하면 2개 밖에 조건식이 없어서 고민을 했다
# 이렇게 코드를 짜게 되면 닫는 괄호가 없는 '(a+b+c' 같은 식이 true로 나온다
# 마지막 return 값을 True 나 False로만 생각하고 있었는데 isEmpty 메소드가 boolean 값을 리턴하기 때문에 
# isEmpty를 마지막 return 빈칸에 써줌으로써 마지막에 스택이 비어있는지 확인할 수 있다.
# 지금까지 주로 return값에는 변수만 써와서 이런 생각을 하지 못했다
# 앞으로는 return 더 잘 사용하자.

