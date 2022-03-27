# * 문제 설명 *

# 리스트를 처음부터 끝까지 순회하는 메서드 traverse() 를 완성하세요.

# 메서드 traverse() 는 리스트를 리턴하되, 
# 이 리스트에는 연결 리스트의 노드들에 들어 있는 데이터 아이템들을 연결 리스트에서의 순서와 같도록 포함합니다. 

# 예를 들어, LinkedList L 에 들어 있는 노드들이 43 -> 85 -> 62 라면, 
# 올바른 리턴 값은 [43, 85, 62] 입니다.

# 이 규칙을 적용하면, 
# 빈 연결 리스트에 대한 순회 결과로 traverse() 메서드가 리턴해야 할 올바른 결과는 [] 입니다.

### 더미노드가 없는 연결리스트로 구현: 헤드가 첫 번째 노드를 가리키도록
class Node:
    def __init__(self, item):
        self.data = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None

    def getAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            return None
        i = 1
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1
        return curr

    def traverse(self):
        if (self.head is None) or (self.nodeCount == 0):
            return []

        curr = self.head
        ret = []
        while curr:   # while (curr is not None):
            ret.append(curr.data)
            curr = curr.next
        return ret

"""
# main.py

LList = LinkedList()
LList.head = Node(43)
Node2 = Node(85)
Node3 = Node(62)
LList.head.next = Node2
Node2.next = Node3
LList.nodeCount = 3

print(LList.traverse()) # 순회 함수

try:
    print(LList.getAt(3).data) # 특정 position 노드 반환 함수
    print(LList.getAt(3).next)
except:
    print("리스트 범위를 넘었습니다!") # getAt() 반환값이 None일 경우
"""