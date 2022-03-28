## 10강 Doubly Linked Lists (양방향 연결 리스트)

- 다음 node로도, 이전 node로도 진행가능

- Node의 구조 확장 -> self.prev = None

- 리스트 처음과 끝에 dummy node 배치  
    self.head = Node(None)  
    self.tail = Node(None)  
    self.head.next = self.tail  
    self.tail.prev = self.head  

- 리스트 순회(traverse) -> while curr.next.next:
- 리스트 역순회(reverse) -> while curr.prev.prev:

- getAt 메소드 수정 -> pos가 self.nodeCount // 2 크고 작은 경우 분리