# 더미 노드 헤더와 트레일러를 갖는 양방향 연결 리스트
# 연결리스트 형태의 큐 ADT 구현 -> class LinkedListQueue: 완성하기

class Node:
    def __init__(self, item):
        self.data = item
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None)	# 더미노드 - 헤더
        self.tail = Node(None)	# 더미노드 - 트레일러
        self.head.prev = None
        self.head.next = self.tail
        self.tail.prev = self.head
        self.tail.next = None

    def __repr__(self):
        if self.nodeCount == 0:
            return 'LinkedList: empty'

        s = ''
        curr = self.head
        while curr.next.next:
            curr = curr.next
            s += repr(curr.data)
            if curr.next.next is not None:
                s += ' -> '
        return s

    def getLength(self):    # size() 메소드
        return self.nodeCount   # nodeCount 속성 반환

    def traverse(self):
        result = []
        curr = self.head
        while curr.next.next:
            curr = curr.next
            result.append(curr.data)
        return result

    def reverse(self):
        result = []
        curr = self.tail
        while curr.prev.prev:
            curr = curr.prev
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

    def popAfter(self, prev):
        curr = prev.next
        next = curr.next
        prev.next = next
        next.prev = prev
        self.nodeCount -= 1
        return curr.data

    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            raise IndexError('Index out of range')

        prev = self.getAt(pos - 1)
        return self.popAfter(prev)

    def concat(self, L):
        self.tail.prev.next = L.head.next
        L.head.next.prev = self.tail.prev
        self.tail = L.tail

        self.nodeCount += L.nodeCount


class LinkedListQueue:
    def __init__(self):
        self.data = DoublyLinkedList()

    def size(self):
        return self.data.getLength()

    def isEmpty(self):
        return self.data.nodeCount == 0

    def enqueue(self, item): # 꼬리에 추가, rear(여기선 tail.prev)에 새 노드 삽입 
        node = Node(item)
        self.data.insertAt(self.data.nodeCount + 1, node)

    def dequeue(self):		 # 머리에서 삭제, front(여기선 head.next)가 가리키는 노드 삭제
        return self.data.popAt(1)

    def peek(self):
        return self.data.getAt(1).data


Q = LinkedListQueue()

Q.enqueue(1)
print(Q.peek())
Q.enqueue(2)
print(Q.peek())
Q.enqueue(3)
print(Q.peek())

Q.dequeue()
print(Q.peek())
Q.dequeue()
print(Q.peek())
Q.dequeue()
print(Q.peek())
