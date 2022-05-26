## 더미노드(헤드,테일)를 갖는 양방향 연결리스트로 구현
##  -> head와 tail 모두 더미노드를 가리킴

## 양방향 연결리스트 2개를 이어주는 concat() 구현하기
## ⭐⭐ 살짝 까다로움. 실수유발 多

'''
두 개의 양방향 연결 리스트를 앞뒤로 이어 붙이는 메서드 concat() 을 구현하세요.

예를 들어, 양방향 연결 리스트 L1 에는 1 -> 2 -> 3 의 원소가 순서대로 들어 있고, 
또다른 양방향 연결 리스트 L2 에는 4 -> 5 의 순서로 원소가 들어 있을 때, 
메서드 호출 L1.concat(L2) 의 결과로 L1 은 1 -> 2 -> 3 -> 4 -> 5 의 양방향 연결 리스트가 됩니다. 

물론, L1 또는 L2 또는 둘 다가 비어 있는 양방향 연결 리스트인 경우도 고려되도록 코드를 작성해야 합니다.
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


    def concat(self, L):    # self == L1,  L == L2
        lastNode = self.tail.prev	# L1의 마지막노드

        if L.head.next == L.tail:	# L2가 빈 리스트일때
            pass
        else: 
            lastNode.next = L.head.next	# L1의 마지막노드와 L2의 첫번째노드 연결작업 (1)
            L.head.next.prev = lastNode	# L1의 마지막노드와 L2의 첫번째노드 연결작업 (2)
            self.tail = L.tail	# L1의 tail 조정

        self.nodeCount += L.nodeCount


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


    def reverse(self):
        ret = []
        curr = self.tail.prev
        while curr.prev:
            ret.append(curr.data)
            curr = curr.prev
        return ret


# case 1
L1 = DoublyLinkedList()
L1.insertAt(1, Node(1))
L1.insertAt(2, Node(2))
L1.insertAt(3, Node(3))
print("L1:", L1.traverse())

L2 = DoublyLinkedList()
L2.insertAt(1, Node(4))
L2.insertAt(2, Node(5))
print("L2:", L2.traverse())

L1.concat(L2)
print("L1(After concat):", L1.traverse())
print("L1 Reverse(After concat):", L1.reverse(), "\n")


# case 2
L1 = DoublyLinkedList()
print("L1:", L1.traverse())
L2 = DoublyLinkedList()
print("L2:", L2.traverse())
L1.concat(L2)
print("L1(After concat):", L1.traverse())
print("L1 Reverse(After concat):", L1.reverse(), "\n")


# case 3
L1 = DoublyLinkedList()
print("L1:", L1.traverse())
L2 = DoublyLinkedList()
L2.insertAt(1, Node(4))
L2.insertAt(2, Node(5))
print("L2:", L2.traverse())
L1.concat(L2)
print("L1(After concat):", L1.traverse())
print("L1 Reverse(After concat):", L1.reverse(), "\n")


# case 4
L1 = DoublyLinkedList()
L1.insertAt(1, Node(1))
L1.insertAt(2, Node(2))
L1.insertAt(3, Node(3))
print("L1:", L1.traverse())
L2 = DoublyLinkedList()
print("L2:", L2.traverse())
L1.concat(L2)
print("L1(After concat):", L1.traverse())
print("L1 Reverse(After concat):", L1.reverse(), "\n")
