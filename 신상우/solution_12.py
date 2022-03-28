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

def solution(S):
    opStack = ArrayStack()
    answer = ''
    for c in S:
        if c.isalpha():
            answer = answer + c
        else: 
            if c == '(' or opStack.isEmpty():
                opStack.push(c)
            elif c in prec:
                if prec[c] > prec[opStack.peek()]: #크면 위로 올린다.
                    opStack.push(c)
                else: #작거나 같으면 빼고 넣는다
                    answer = answer + opStack.pop()
                    opStack.push(c)
            else:
                while opStack.peek() != '(':
                    answer = answer + opStack.pop()
                opStack.pop()
                     
    while not opStack.isEmpty():
        answer = answer + opStack.pop()
    return answer


#어떻게 이런 정답을 생각했는지?

#일단 알파벳이면 바로 추가하고 연산자이면 스택에 넣어야한다. 
#그래서 크게 알파벳과 연산자로 나눈다.
#연산자는 우선순위에 따라서 어떻게 스택에 뽑고 넣을 것인지 조건을 나눈다. ex) 스택의 Top과 c(연산자) 우선 순위 비교 
#스택에 조건에 맞게 채우고 차례대로 뽑는다. 뽑는 경우는 두가지
# 1. ')' 닫는 괄호가 있을 때(올바르게 구성되지 않은 수식은 제공되지 않는다고 가정했기에 알파벳과 나머지 연산자가 아니면 ')', 즉 else)
#  -> '(', 여는 괄호를 만날 때까지 뽑기.(괄호가 이중으로 되어있어도 첫 괄호에서 걸림) 마지막에 여는 괄호 삭제
# 2. for문이 끝났을 때
# for 문 안에서 이미 괄호에 대한 처리는 끝났고 스택에 쌓여있는대로 스택이 비어있지 않을 때까지 뽑아서 채우면 됨

#어떤 생각에서 막혔는지?
#str에는 append를 쓸 수 없다. 
#연산자 중에 prec사전 안에 포함되는지 체크를 안하고 조건문을 나눴더니 prec[c]에 ')'이 들어갔을 때 오류가 생김

#다음에는 어떻게 풀 수 있는지?, 더 좋은 방법은 없을까?

#만약 올바르게 구성되지 않은 수식도 제공된다면 elif 문을 써서 조건을 더 확실히 해줘야한다. 
#if 문이 중첩되어 있는데 좀 더 깔끔하게 짤 순 없을까?

# S = "(A+B)*(C+D)"
# a = "A*B+C"
# b = "A+B*C"
# c = "A+B+C"
# d = "(A+B)*C"
# e = "A*(B+C)"
# print(solution(S))
# print(solution(a))
# print(solution(b))
# print(solution(c))
# print(solution(d))
# print(solution(e))



