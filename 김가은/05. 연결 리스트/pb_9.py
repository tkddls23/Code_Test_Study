### 더미노드가 있는 연결리스트로 구현: 헤드가 더미노드를 가리킴
## popAfter와 popAt 구현

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


    def insertAfter(self, prev, newNode):   # prev 다음 노드로 삽입
        newNode.next = prev.next
        if prev.next is None:
            self.tail = newNode
        prev.next = newNode
        self.nodeCount += 1
        return True


    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        if pos != 1 and pos == self.nodeCount + 1:
            prev = self.tail
        else:
            prev = self.getAt(pos - 1)
        return self.insertAfter(prev, newNode)


    def popAfter(self, prev):   # prev 다음 노드를 삭제하는 메소드
        if prev.next is None:    # 빈 리스트 or prev가 마지막노드(prev 다음 노드 존재X)
            return None

        delNode = prev.next
        prev.next = delNode.next
        
        if delNode.next is None:    # 마지막 노드를 삭제할때 tail 조정
            self.tail = prev

        self.nodeCount -= 1
        return delNode.data


    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            raise IndexError

        prev = self.getAt(pos - 1)
        return self.popAfter(prev)


LList = LinkedList()
LList.insertAt(1, Node(43))
LList.insertAt(2, Node(85))
LList.insertAt(3, Node(62))
print(LList.traverse())	# [43, 85, 62]
print(LList.popAt(1))	# 첫 번째 노드 삭제
print(LList.traverse())
print(LList.popAt(2))	# 마지막 노드 삭제
print(LList.traverse())
print(LList.popAt(1))	# 유일한 노드 삭제
print(LList.traverse())