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


    def traverse(self):
        result = []
        curr = self.head
        while curr is not None:
            result.append(curr.data)
            curr = curr.next
        return result


    ## 내가 구현한 삽입 함수
	def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        if pos == 1:  # 첫 번째 노드로 삭제할때
            newNode.next = self.head  # None
            self.head = newNode
        else:  # 2 <= pos <= self.nodeCount+1
            prev = self.getAt(pos - 1)
            newNode.next = prev.next
            perv.next = newNode

        if pos == self.nodeCount + 1:   # 마지막 노드로 삭제할때
            self.tail = newNode

        self.nodeCount += 1
        return True