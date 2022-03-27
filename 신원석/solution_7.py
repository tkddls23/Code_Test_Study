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
        curr = self.head  # 현재위치를 head로 맞춤
        List = []

        if self.nodeCount == 0:  # list가 비어있는 경우
            return List
        else:  # list안에 하나라도 들어있는 경우
            List.append(curr.data)
            while True:  # curr이 tail에 도착할때까지 반복
                curr = curr.next
                List.append(curr.data)
                if curr == self.tail:
                    return List

# 이 solution 함수는 그대로 두어야 합니다.


def solution(x):
    return 0
