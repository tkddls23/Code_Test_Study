## 11강 Stacks (스택)

- 자료를 보관할 수 있는 선형 자료구조

- push 연산 : 한 쪽 끝에서 밀어넣어야 함
- pop 연산 : 같은 쪽에서 뽑아 꺼내야 함  
==> 후입선출(LIFO: Last-In First-Out)  

- 발생 가능 오류  
    1) stack underflow : 비어있는 스택에서 데이터 원소를 꺼내려 할 때  
    2) stack overflow : 꽉 찬 스택에 데이터 원소를 넣으려 할 때  

- 스택의 추상적 자료구조 구현    
    ❗️연산 정의  
        -> size() 현재 스택에 들어 있는 데이터 원소의 수 구함  
        -> isEmpty() 현재 스택이 비어있는지 판단  
        -> push(x) 데이터 원소 x를 스택에 추가  
        -> pop() 스택 맨 위의 데이터 원소 제거(반환)  
        -> peek() 스택 맨 위의 데이터 원소 반환(제거x)  

    1) 배열 이용하여 구현  
        -> size - return len(self.data)  
        -> isEmpty - return self.size() == 0  
        -> push(x) - self.data.append(x)  
        -> pop - return self.data.pop()  
        -> peek - return self.data[-1]  
    2) 양방향 연결 리스트 이용하여 구현  
        -> size - return self.data.getLength()  
        -> isEmpty - return self.size() == 0  
        -> push(x) - node = Node(x) + self.data.insertAt(self.size()+1, node)  
        -> pop - return self.data.popAt(self.size())  
        -> peek - return self.data.getAt(self.size()).data  

- 파이썬 제공 라이브러리 : from pythonds.basic.stack import Stack