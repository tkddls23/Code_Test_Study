# 18-2번 이진트리 선위순회 메소드 preorder() 구현

class Node:
    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None


    def inorder(self):
        traversal = []
        if self.left:
            traversal += self.left.inorder()
        traversal.append(self.data)
        if self.right:
            traversal += self.right.inorder()
        return traversal


    def preorder(self):
        travResult = []
        
        travResult.append(self.data)
        if self.left:
            travResult += self.left.preorder() # 리스트 덧셈연산 (리스트 확장)
        if self.right:
            travResult += self.right.preorder()

        return travResult


class BinaryTree:
    def __init__(self, r):
        self.root = r


    def inorder(self):
        if self.root:
            return self.root.inorder()
        else:
            return []


    def preorder(self):
        if self.root:
            return self.root.preorder()
        else:
            return []


r = Node(1);
BinaryTree(r);

r.left = Node(2);
r.right = Node(3);

r.left.left = Node(4);
r.left.right = Node(5);
r.right.right = Node(6);
r.right.right.left = Node(7);

print(r.preorder())
