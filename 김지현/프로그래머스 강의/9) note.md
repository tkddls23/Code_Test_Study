- constructor

```python
class Node:

    def __init__(self, item):
        self.data = item
        self.next = None

class LinkedList:

    def __init__(self):
        self.nodeCount = 0 # head 미포함
        self.head = Node(None) # dummy node 추가
        self.tail = None
        self.head.next = self.tail
```

### Operations

- 리스트 순회

```python
def traverse(self):
    result = []

    curr = self.head
    while curr.next:
        curr = curr.next
        result.append(curr.data)

    return result
```

- k번째의 원소 얻기

```python
def getAt(self, pos):
    if pos < 0 or pos > self.nodeCount: # dummy head를 get할 수 있도록
        return None

    i = 0
    curr = self.head
    while i < pos: # pos번
        curr = curr.next
        i += 1

    return curr
```

- 원소 삽입

```python
# prev의 다음 node에 newNode 삽입
def insertAfter(self, prev, newNode):
    newNode.next = prev.next
    if prev.next is None: # 마지막에 삽입 시
        self.tail = newNode

    prev.next = newNode

    self.nodeCount += 1
    return True
```

```python
def insertAt(self, pos, newNode):
    if pos < 1 or pos > self.nodeCount + 1:
        return False

    if pos != 1 and pos == self.nodeCount + 1: # 빈 리스트가 아니고, 마지막에 삽입하는 경우
        prev = self.tail
    else:
        prev = self.getAt(pos - 1)

    return self.insertAfter(prev, newNode)
```

- 원소 삭제

```python
# prev의 다음 node 삭제
def popAfter(self, prev):
    if prev == self.tail: # popAt에서 호출 시에는 always skip
        return None

    curr = prev.next
    nextNode = curr.next
    prev.next = nextNode # prev 노드와 next 노드를 연결

    if nextNode == None: # 마지막 원소(self.tail)를 삭제하는 경우
        self.tail = prev if prev != self.head else None

    self.nodeCount -= 1
    return curr.data
```

```python
def popAt(self, pos):
    if pos < 1 or pos > self.nodeCount:
        raise IndexError

    prev = self.getAt(pos - 1)
    return self.popAfter(prev)
```

- 리스트 연결

```python
def concat(self, L):
    self.tail.next = L.head.next
    if L.tail:
        self.tail = L.tail

    self.nodeCount += L.nodeCount
```
