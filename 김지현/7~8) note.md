## 추상적 자료형(Abstract data type)

- 자료 구조가 따라야 할 규칙 like class
- 내부 구현 신경 X
- 2가지 제공
  1. 저장하는 data - ex) 정수, 문자열, 레코드
  2. A set of operations that should be done - ex) 삽입, 삭제, 순회, 정렬, 탐색

# 자료구조

## 연결 리스트

- constructor

```python
class Node:

    def __init__(self, item):
        self.data = item
        self.next = None

class LinkedList:

    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None
```

- 각 Node가 다른 node를 가리킴
  - Node ⊃ data + link

|                | 배열                | 연결 리스트             |
| -------------- | ------------------- | ----------------------- |
| 저장 공간      | 연속한 위치(인덱스) | 임의의 위치             |
| 특정 원소 참조 | 간편(L[i]) - O(1)   | 선형 탐색과 유사 - O(n) |

- 장점: 삽입/삭제 유연

## 연결 리스트의 추상적 자료형

- ⊃ Head + tail + the number of nodes + possible operations

### Operations

- 길이 getter: `.nodeCount`
- 원소 삽입/삭제: `.head` or `.tail` 변경, `.next` 연결, `.nodeCount`변경

  - 삽입

    - 맨 앞 삽입: O(1)
    - 중간 삽입: O(n)
    - 맨 끝 삽입: O(1)

    ```python
    def insertAt(self, pos, newNode): # 1 <= pos <= nodeCount + 1
            if pos < 1 or pos > self.nodeCount + 1:
                return False

            if pos == 1: # 빈 리스트에 삽입 시
                newNode.next = self.head
                self.head = newNode

            else:
                if pos == self.nodeCount + 1: # 맨 끝에 삽입 시
                    prev = self.tail
                else:
                    prev = self.getAt(pos - 1)
                newNode.next = prev.next # 기존 pos번째 node와 link 연결
                prev.next = newNode # 기존 pos-1번째 node와 link 연결

            if pos == self.nodeCount + 1: # 빈 리스트에 삽입 시
                self.tail = newNode

            self.nodeCount += 1
            return True
    ```

  - 삭제

    - 맨 앞 삭제: O(1)
    - 중간 삭제: O(n)
    - 맨 끝 삭제: O(n)

    ```python
    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            raise IndexError

        prev = self.getAt(pos - 1)
        curr = prev.next if prev else self.getAt(pos)

        if pos == 1:
            self.head = curr.next
            if self.nodeCount == 1:
                self.tail = self.head

        else:
            if pos == self.nodeCount:
                self.tail = prev
            prev.next = curr.next

        self.nodeCount -= 1
        return curr.data
    ```

- k번째의 원소 얻기

  ```python
  def getAt(self, pos):
      if pos <= 0 or pos > self.nodeCount:
          return None

      i = 1
      curr = self.head
      while i < pos: # pos-1 번
          i += 1
          curr = curr.next

      return curr # pos번째 node
  ```

- 리스트 순회

  ```python
  def traverse(self):
      data = []

      curr = self.head
      while curr:
          data.append(curr.data)
          curr = curr.next

      return data
  ```

- 리스트 연결

  ```python
  def concat(self, L):
      self.tail.next = L.head
      if L.tail: # if L is not empty
          self.tail = L.tail

      self.nodeCount += L.nodeCount
  ```

[자료구조 3 - 추상 자료형(Abstract Data Type)](https://jinkpark.tistory.com/77)
