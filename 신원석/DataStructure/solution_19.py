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
        traversal = [] # 순회 list
        q = ArrayQueue() # 빈 queue
        
        if self.root: # tree 체크
            q.enqueue(self.root)
        
        while not q.isEmpty(): # queue가 빌때까지
            node = q.dequeue() 
            traversal.append(node.data)
            
            if node.left: # queue에서 빼넨 node에 left check
                q.enqueue(node.left)
            if node.right:  # queue에서 빼넨 node에 right check
                q.enqueue(node.right)
            
        
        return traversal


def solution(x):
    return 0