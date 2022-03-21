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
        data = []
        if self.nodeCount == 0:
            return data

        curr = self.head

        while True:
            data.append(curr.data)
            if curr == self.tail:
                break

            curr = curr.next

        return data


# 이 solution 함수는 그대로 두어야 합니다.
def solution(x):
    ins = LinkedList()
    return ins.traverse()