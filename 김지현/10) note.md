# 이중 연결 리스트

- Node는 양쪽에 link를 가짐
- 데이터를 담고 있는 node들은 모두 같은 모양
- constructor

```python
  class Node:
      def __init__(self, item):
          self.data = item
          self.prev = None
          self.next = None

  class DoublyLinkedList:
      def __init__(self):
          self.nodeCount = 0
          self.head = Node(None)
          self.tail = Node(None)
          self.head.prev = None
          self.head.next = self.tail
          self.tail.prev = self.head
          self.tail.next = None
```

## operations

- 리스트 순회

```python
def traverse(self):
    result = []
    curr = self.head

    while curr.next.next:
        curr = curr.next
        result.append(curr.data)

    return result
```

- 리스트 역순회

```python
def reverse(self):
    result = []
    curr = self.tail

    while curr.prev.prev:
        curr = curr.prev
        result.append(curr.data)

    return result
```

- k번째 원소 얻기: 일반 연결 리스트와 동일 or

```python
def getAt(self, pos):
    if pos < 0 or pos > self.nodeCount:
        return None

    if pos > self.nodeCount // 2:
        i = 0
        curr = self.tail
        while i < self.nodeCount - pos + 1:
            curr = curr.prev
            i += 1

    else:
        i = 0
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1

    return curr
```

- 특정 원소의 뒤에 원소 삽입

```python
def insertAfter(self, prev, newNode):
    next = prev.next

    newNode.prev = prev
    newNode.next = next

    prev.next = newNode
    next.prev = newNode

    self.nodeCount += 1
    return True
```

```python
def insertAt(self, pos, newNode):
    if pos < 1 or pos > self.nodeCount + 1:
        return False

    prev = self.getAt(pos - 1)
    return self.insertAfter(prev, newNode)
```

- 특정 원소의 앞에 삽입

```python
def insertBefore(self, next, newNode):
    prev = next.prev

    newNode.prev = prev
    newNode.next = next

    prev.next = newNode
    next.prev = newNode

    self.nodeCount += 1
    return True
```

```python
def insertAt(self, pos, newNode):
    if pos < 1 or pos > self.nodeCount + 1:
        return False

    next = self.getAt(pos)
    return self.insertBefore(next, newNode)
```

- 특정 원소의 뒤의 원소 삭제

```python
def popAfter(self, prev):
    delNode = prev.next
    next = delNode.next

    prev.next = next
    next.prev = prev

    self.nodeCount -= 1
    return delNode.data
```

- 특정 원소의 앞의 원소 삭제

```python
def popBefore(self, next):
    delNode = next.prev
    prev = delNode.prev

    prev.next = next
    next.prev = prev

    self.nodeCount -= 1
    return delNode.data
```

```python
def popAt(self, pos):
    if pos < 1 or pos > self.nodeCount:
        raise IndexError

    next = self.tail if pos == self.nodeCount else self.getAt(pos + 1) # pos == self.nodeCount 이면 self.getAt(pos + 1) == None 이므로
    return self.popBefore(next)
```

- 리스트 연결

```python
def concat(self, L):
    L.head.next.prev = self.tail.prev
    self.tail.prev.next = L.head.next

    self.tail = L.tail
    self.nodeCount += L.nodeCount
```
