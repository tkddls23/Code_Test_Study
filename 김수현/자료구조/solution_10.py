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
    newNode.next = next
    newNode.prev = prev
    next.prev = newNode
    prev.next = newNode
    self.nodeCount += 1
    return True


# 10-3

def popAfter(self, prev):
    curr = prev.next
    next = curr.next

    prev.next = next
    next.prev = prev

    self.nodeCount -= 1
    return curr.data


def popBefore(self, next):
    curr = next.prev
    prev = curr.prev

    prev.next = next
    next.prev = prev

    self.nodeCount -= 1
    return curr.data


def popAt(self, pos):
    if pos < 1 or pos > self.nodeCount:
        raise IndexError

    prev = self.getAt(pos - 1)
    return self.popAfter(prev)


# 10-4

def concat(self, L):
    self.tail.prev.next = L.head.next
    L.head.next.prev = self.tail.prev
    self.tail = L.tail

    self.nodeCount += L.nodeCount