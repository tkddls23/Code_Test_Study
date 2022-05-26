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


'''
인자 S의 각 문자(s)를 총 4가지 케이스로 세분화
'''
def solution(S):
    opStack = ArrayStack()
    answer = ''

    for s in S:
        # 1. 현재 s가 영문인 경우
        if s not in prec and s != ")": # .isalpha()도 가능
            answer += s
            continue

        # 2. 영문이 아닌 경우

        # 2-1. 여는 괄호
        if s == "(":
            opStack.push(s)
            continue

        # 2-2. 닫는 괄호
        if s == ")":
            while True:
                delData = opStack.pop() # 스택에서 지울 요소
                if delData == "(": # delData가 ( 일 때까지 반복문 실행
                    break
                answer += delData # ( 외의 연산자들(괄호 안에 있었던) 출력
            continue

        # 2-3. 그 외 연산자
        while opStack.size() and prec[s] <= prec[opStack.peek()]: # 현재 s와 스택 원소들의 우선순위 비교
            answer += opStack.pop() # 현재 s의 우선순위가 낮거나 같다면, 스택 원소를 pop하여 출력

        opStack.push(s) # 현재 s는 스택에 push (현재 s의 우선순위가 높은 경우, 기존 스택이 비어 있던 경우 포함)


    # for문 종료 시, 남은 연산자들 출력
    while not opStack.isEmpty():
        answer += opStack.pop()

    return answer


print(solution("(A+B)*(C+D)")) # "AB+CD+*"
print(solution("A*B+C")) # "AB*C+"
print(solution("A+B*C")) # "ABC*+"
print(solution("A+B+C")) # "AB+C+"
print(solution("(A+B)*C")) # "AB+C*"
print(solution("A*(B+C)")) # "ABC+*"