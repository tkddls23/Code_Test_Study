## 추상적 자료형(Abstract data type)

- 자료 구조가 따라야 할 규칙 like class
- 내부 구현 신경 X
- 2가지 제공
  1. 저장하는 data - ex) 정수, 문자열, 레코드
  2. A set of operations that should be done - ex) 삽입, 삭제, 순회, 정렬, 탐색

# 자료구조

## 연결 리스트

- 각 Node가 다른 node를 가리킴
  - Node ⊃ data + link

|                | 배열                | 연결 리스트             |
| -------------- | ------------------- | ----------------------- |
| 저장 공간      | 연속한 위치(인덱스) | 임의의 위치             |
| 특정 원소 참조 | 간편(L[i]) - O(1)   | 선형 탐색과 유사 - O(n) |

## 연결 리스트의 추상적 자료형

- ⊃ Head + tail + the number of nodes + possible operations

### Operations

- 원소 삽입/삭제
- 길이 getter
- 리스트 순회
- k번째의 특정 원소 참조
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
- 두 리스트 합치기

[자료구조 3 - 추상 자료형(Abstract Data Type)](https://jinkpark.tistory.com/77)
