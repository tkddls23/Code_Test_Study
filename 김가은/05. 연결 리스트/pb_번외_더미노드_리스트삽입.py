### 더미노드가 있는 연결리스트로 구현: 헤드가 더미노드를 가리킴
## insertAfter와 insertAt 구현함


class Node:
    def __init__(self, item):
        self.data = item
        self.next = None


class LinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None)  # 더미노드가 있는 연결리스트
        self.tail = None
        self.head.next = self.tail


    def traverse(self):
        result = []
        curr = self.head
        while curr.next:
            curr = curr.next
            result.append(curr.data)
        return result


    def getAt(self, pos):
        if pos < 0 or pos > self.nodeCount: # 더미노드(헤드) 반환을 위해 pos == 0 허용
            return None

        i = 0
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1

        return curr


    ## 내가 구현한 함수
    def insertAfter(self, prev, newNode):   # prev 다음 노드로 삽입
        if prev.next is None:   # 마지막 노드로 삽입할때
            self.tail = newNode
        newNode.next = prev.next
        prev.next = newNode
        self.nodeCount += 1
        return True
        

    ## 내가 구현한 함수
    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        prev = self.getAt(pos - 1)
        return self.insertAfter(prev, newNode)   # 마지막 노드 삽입 시 tail 조정은 insertAfter에서 이뤄짐