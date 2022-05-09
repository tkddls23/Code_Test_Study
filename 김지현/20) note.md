# 이진 탐색 트리의 추상적 자료형

- 모든 노드에 대해, left subtree의 값들 < 현재 노드의 값 < right subtree의 값들인 이진 트리
  - 중복 값 없다고 가정
- not always O(log n)
- 각 노드는 (key, value) 쌍 → key로 데이터 검색 가능, 복잡한 데이터 레코드로 확장 가능
- 장점: 원소의 추가/삭제 용이
- 단점: 공간 소요 큼

<br>

- `.insert(key, data)`
- `.remove(key)`
- `.lookup(key)`
- `.inorder()`: key 순서대로 원소 나열
- `.min()`, `.max()`: 최소 key/최대 key 가지는 원소 탐색

```python
class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None

    def insert(self, key, data):
        if key < self.key:
            if self.left:
                self.left.insert(key, data)
            else:
                self.left = Node(key, data)

        elif key > self.key:
            if self.right:
                self.right.insert(key, data)
            else:
                self.right = Node(key, data)

        else:
            raise KeyError('This key already exists')


    def lookup(self, key, parent=None):
        if key < self.key:
            return self.left.lookup(key, self) if self.left else None, None
        elif key == self.key:
            return self, parent
        else:
            return self.right.lookup(key, self) if self.right else None, None

    def inorder(self):
        traversal = []
        if self.left:
            traversal += self.left.inorder()
        traversal.append(self)
        if self.right:
            traversal += self.right.inorder()
        return traversal

    def min(self):
        return self.left.min() if self.left else self


class BinSearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key, data):
        if self.root:
            self.root.insert(key, data)
        else:
            self.root = Node(key, data)

    def lookup(self, key):
        return self.root.lookup(key) if self.root else None, None

    def inorder(self):
        if self.root:
            return self.root.inorder()
        else:
            return []

    def min(self):
        return self.root.min() if self.root else None
```
