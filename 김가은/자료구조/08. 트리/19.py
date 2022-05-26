# 이진 트리 - 넓이 우선 순회 [= 레벨 순회]

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
        result = []
        
        if self.root:
            Q = ArrayQueue()
            Q.enqueue(self.root) # 노드 채로 enqueue

            while not Q.isEmpty():
                x = Q.dequeue()
                result.append(x.data) ### dequeue 하고선 노드의 data를 결과리스트에 추가
                
                if x.left:
                    Q.enqueue(x.left)
                if x.right:
                    Q.enqueue(x.right)

            return result        
            
        else:
            return []


r = Node(1);
BTree = BinaryTree(r);

r.left = Node(2);
r.right = Node(3);

r.left.left = Node(4);
r.left.right = Node(5);
r.right.right = Node(6);
r.right.right.left = Node(7);

print(BTree.bft())