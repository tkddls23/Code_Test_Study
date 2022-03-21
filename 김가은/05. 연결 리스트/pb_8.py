## 특정 위치 노드를 삭제 후 값을 반환하는 메소드 popAt(self, pos) 구현하기
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


    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        if pos == 1:
            newNode.next = self.head
            self.head = newNode

        else:
            if pos == self.nodeCount + 1:
                prev = self.tail
            else:
                prev = self.getAt(pos - 1)
            newNode.next = prev.next
            prev.next = newNode

        if pos == self.nodeCount + 1:
            self.tail = newNode

        self.nodeCount += 1
        return True


    def popAt(self, pos): # 리스트에서 pos번째 노드를 삭제 후 반환하는 메소드 
        if pos < 1 or pos > self.nodeCount:
            raise IndexError        

        if pos == 1: # 첫 번째 노드 삭제 시 head 조정
            delNode = self.head
            self.head = self.head.next
            if self.nodeCount == 1: # 유일한 노드 삭제 시의 tail 조정
                self.tail = self.head
                
        else:  # 2 <= pos <= self.nodeCount
            prev = self.getAt(pos - 1)
            delNode = prev.next
            prev.next = delNode.next

        if pos != 1 and pos == self.nodeCount: # 마지막 노드(tail이 가리키는 노드) 삭제 시 tail 조정
            self.tail = prev
            
        self.nodeCount -= 1
        return delNode.data
        

    def traverse(self):
        result = []
        curr = self.head
        while curr is not None:
            result.append(curr.data)
            curr = curr.next
        return result

"""
# main.py

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
"""