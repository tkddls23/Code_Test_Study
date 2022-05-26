## 더미노드(헤드,테일)를 갖는 양방향 연결리스트로 구현
##  -> head와 tail 모두 더미노드를 가리킴

# 주어진 next 앞에 노드를 추가하는 insertBefore()를 구현하라.

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


    def insertBefore(self, next, newNode):  # next의 앞 노드에 삽입하는 메소드
        prev = next.prev
        
        newNode.prev = prev
        newNode.next = next
        prev.next = newNode
        next.prev = newNode

        self.nodeCount += 1
        return True