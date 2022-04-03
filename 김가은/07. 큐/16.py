'''
양방향 연결리스트를 기반으로 우선순위 큐 ADT를 구현하시오
Enqueue 할 때 우선순위를 유지해야 하며, Data 자료형은 정수이며 숫자가 작을수록 높은 우선순위라고 가정
-> class PriorityQueue에서 주어진 dequeue()를 고려하여 enqueue()를 완성하시오
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

    def getLength(self):
        return self.nodeCount

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
            return None

        prev = self.getAt(pos - 1)
        return self.popAfter(prev)

    def concat(self, L):
        self.tail.prev.next = L.head.next
        L.head.next.prev = self.tail.prev
        self.tail = L.tail

        self.nodeCount += L.nodeCount


class PriorityQueue:
    def __init__(self):
        self.queue = DoublyLinkedList()


    def size(self):
        return self.queue.getLength()

    def isEmpty(self):
        return self.size() == 0

    def enqueue(self, x):   # 인자 x는 정수
        newNode = Node(x)
        curr = self.queue.head

        while curr.next.next is not None and curr.next.data > x:
            curr = curr.next

        self.queue.insertAfter(curr, newNode)   # curr 다음 노드에 새 노드 삽입

    def dequeue(self):
        return self.queue.popAt(self.queue.getLength())

    def peek(self):
        return self.queue.getAt(self.queue.getLength()).data


PQ = PriorityQueue()
PQ.enqueue(1)
PQ.enqueue(4)
print(PQ.queue.traverse())

PQ.enqueue(3)
print(PQ.queue.traverse())

PQ.enqueue(2)
print(PQ.queue.traverse())

PQ.enqueue(7)
print(PQ.queue.traverse())
PQ.enqueue(6)
print(PQ.queue.traverse())
