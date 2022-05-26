class ArrayQueue:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        return self.data.pop(0)

    def peek(self):
        return self.data[0]


class Node:

    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self, r):
        self.root = r


    def bft(self):
        traversal = []
        q = ArrayQueue()
        if self.root:
            q.enqueue(self.root)

        # 큐가 비어있지 않은 동안
        while not q.isEmpty():
            visitedNode = q.dequeue()
            traversal.append(visitedNode.data)

            if visitedNode.left:
                q.enqueue(visitedNode.left)
            if visitedNode.right:
                q.enqueue(visitedNode.right)

        return traversal


def solution(x):
    return 0