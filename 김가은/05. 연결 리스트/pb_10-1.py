## 더미노드(헤드,테일)를 갖는 양방향 연결리스트로 구현
##  -> head와 tail 모두 더미노드를 가리킴

'''
reverse() 메소드 구현하기

양방향 연결 리스트를 끝에서부터 시작해서 맨 앞에 도달할 때까지 
(tail 방향에서 head 방향으로) 순회하면서, 
방문하게 되는 node 에 들어 있는 data item 을 순회 순서에 따라 리스트에 담아 리턴
'''

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


    def reverse(self):
        ret = []
        curr = self.tail.prev

        while curr.prev:	# head.prev == None
            ret.append(curr.data)
            curr = curr.prev

        return ret


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


DLList = DoublyLinkedList()
DLList.insertAt(1, Node(43))
DLList.insertAt(2, Node(85))
DLList.insertAt(3, Node(62))
print(DLList.reverse())