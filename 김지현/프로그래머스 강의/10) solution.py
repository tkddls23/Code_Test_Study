# 10-1
def reverse(self):
    result = []
    curr = self.tail

    while curr.prev.prev:
        curr = curr.prev
        result.append(curr.data)

    return result


# 10-2
def insertBefore(self, next, newNode):
    prev = next.prev

    # newNode의 prev/next 조정
    newNode.prev = prev
    newNode.next = next

    # prev/next node의 prev/next 조정
    prev.next = newNode
    next.prev = newNode

    self.nodeCount += 1
    return True


# 10-3
def popAfter(self, prev):
    # if prev == self.tail:
    #     return None

    delNode = prev.next
    next = delNode.next

    # prev/next node 서로 연결
    prev.next = next
    next.prev = prev

    self.nodeCount -= 1
    return delNode.data


def popBefore(self, next):
    # if next == self.head:
    #     return None
    
    delNode = next.prev
    prev = delNode.prev

    # prev/next node 서로 연결
    prev.next = next
    next.prev = prev

    self.nodeCount -= 1
    return delNode.data   
    

def popAt(self, pos):
    if pos < 1 or pos > self.nodeCount:
        raise IndexError

    next = self.tail if pos == self.nodeCount else self.getAt(pos + 1) # pos == self.nodeCount 이면 self.getAt(pos + 1) == None 이므로
    return self.popBefore(next)


# 10-4
def concat(self, L):
    # L의 첫 데이터 node 자리와 self의 마지막 데이터 node 자리 연결
    L.head.next.prev = self.tail.prev
    self.tail.prev.next = L.head.next

    # 리스트가 서로 연결되면 tail이 두 개가 되므로
    self.tail = L.tail
    self.nodeCount += L.nodeCount