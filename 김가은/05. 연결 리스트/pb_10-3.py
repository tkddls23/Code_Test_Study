## 더미노드(헤드,테일)를 갖는 양방향 연결리스트로 구현
##  -> head와 tail 모두 더미노드를 가리킴

# 노드를 삭제하는 메소드 popAfter(), popBefore(), popAt() 구현하기

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


    def traverse(self):
        result = []
        curr = self.head
        while curr.next.next:
            curr = curr.next
            result.append(curr.data)
        return result


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


    def insertAfter(self, prev, newNode):
        next = prev.next
        newNode.prev = prev
        newNode.next = next
        prev.next = newNode
        next.prev = newNode
        self.nodeCount += 1
        return True


    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        prev = self.getAt(pos - 1)
        return self.insertAfter(prev, newNode)


    def popAfter(self, prev):   # 주어진 노드(prev) 뒤의 노드를 삭제 후 데이터 반환
        if prev.next is None or prev.next == self.tail:  # 빈 리스트일때, prev가 tail일때, prev가 마지막 노드일때(삭제할 노드X)
            return None
        
        delNode = prev.next

        prev.next = delNode.next
        delNode.next.prev = prev
        
        self.nodeCount -= 1
        return delNode.data


    def popBefore(self, next):  # 주어진 노드(next) 앞의 노드를 삭제 후 데이터 반환
        if next.prev is None or next.prev == self.head:  # 빈 리스트일때, next가 head일때, next가 첫 번째 노드일때(삭제할 노드X)
            return None

        delNode = next.prev

        delNode.prev.next = next
        next.prev = delNode.prev

        self.nodeCount -= 1
        return delNode.data


    def popAt(self, pos):       # pos 위치의 노드 삭제 후 데이터 반환
        if pos < 1 or pos > self.nodeCount:
            raise IndexError

        prev = self.getAt(pos - 1)

        return self.popAfter(prev)


DLList = DoublyLinkedList()
a = Node(43)
b = Node(85)
c = Node(62)
DLList.insertAt(1, a)
DLList.insertAt(2, b)
DLList.insertAt(3, c)

##print(DLList.popAfter(DLList.head))
##print(DLList.popAfter(a))
##print(DLList.popAfter(b))
##print(DLList.popAfter(c))
##print(DLList.popAfter(DLList.tail))
##
##print(DLList.popBefore(DLList.head))
##print(DLList.popBefore(a))
##print(DLList.popBefore(b))
##print(DLList.popBefore(c))
##print(DLList.popBefore(DLList.tail))

print(DLList.popAt(1))  # 첫 번째 노드 삭제
print(DLList.popAt(2))  # 마지막 노드 삭제
print(DLList.popAt(1))  # 유일한 노드 삭제