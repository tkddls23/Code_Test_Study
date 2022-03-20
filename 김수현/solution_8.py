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


    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            raise IndexError

        if pos == 1:
            curr, self.head = self.head, curr.next
            if self.nodeCount == 1:
                self.tail = None
        else:
            prev = self.getAt(pos-1)
            curr, prev.next = prev.next, curr.next
            if pos == self.nodeCount:
                self.tail = prev
        
        self.nodeCount -= 1
        return True

    # pos가 1일 때, curr을 self.head로 하고 self.head를 curr.next로 함(이때, 만약 리스트길이가 1이면 self.tail값 None으로)
    # 그 외, prev를 pos-1의 노드로 하고, curr은 prev.next, prev.next는 curr.next로 함(이때, 만약 pos가 마지막요소라면 self.tail값 prev로)


    def traverse(self):
        result = []
        curr = self.head
        while curr is not None:
            result.append(curr.data)
            curr = curr.next
        return result


def solution(x):
    return 0