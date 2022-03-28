# 스택

- 데이터를 보관하는 선형 구조
- 한 쪽 끝으로 밀어 넣고(push 연산), 같은 쪽에서 뽑아 꺼내야 함(pop 연산)
  - 후입선출(LIFO, Last-In-First-Out) 방식
- `S = Stack()` - empty stack

→ `S.push(A)`, `.S.push(B)` - 원소 A, B 추가

→ `r1 = S.pop()` - 원소 B 삭제

→ `r2 = S.pop()` - 원소 A 삭제

- 오류

  - Stack underflow: empty stack에서 데이터 삭제 시 - `r3 = S.pop()`
  - Stack overflow: full stack에 데이터 추가 시 - `S.push(C)`

- 라이브러리

```python
from pythonds.basic.stack import Stack
S= Stack()
dir(S)
```

# 스택의 추상적 자료형

### Operations

- `.size()`: 원소의 수
- `.isEmpty()`: 스택이 비어 있는지의 여부
- `.push(x)`: 원소 x 추가
- `.pop()`: 마지막 (맨 위) 원소를 삭제/반환
- `.peek()`: 마지막 (맨 위) 원소를 반환 (삭제 x)

## By 배열

- constructor

```python
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
```

## By 이중 연결 리스트

- constructor

```python
  class LinkedListStack:
      def __init__(self):
          self.data = DoublyLinkedList()

      def size(self):
          return self.data.nodeCount

      def isEmpty(self):
          return self.size() == 0

      def push(self, item):
          node = Node(item)
          self.data.insertAt(self.size() + 1, node)

      def pop(self):
          return self.data.popAt(self.size())

      def peek(self):
          return self.data.getAt(self.size()).data
```
