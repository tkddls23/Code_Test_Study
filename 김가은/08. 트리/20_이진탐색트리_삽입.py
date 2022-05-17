# 20강 이진탐색트리 - insert(key, data) 구현
# 중복된 키는 존재하지 않는다고 가정 - 중복키 삽입 시 KeyError 발생시키기

class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None


    def insert(self, key, data): # (키, 원소)쌍 맞는 위치에 삽입
        # self 노드의 키값이 비교대상. self를 옮겨가며 삽입 위치를 찾음

        if self.key == key: # 중복된 키는 삽입할 수 X
            raise KeyError


        elif self.key > key:
            if self.left:
                self.left.insert(key, data)
            else:
                self.left = Node(key, data) # 노드 삽입

        elif self.key < key:
            if self.right:
                self.right.insert(key, data)
            else:
                self.right = Node(key, data) # 노드 삽입


    def inorder(self):
        traversal = []
        if self.left:
            traversal += self.left.inorder()
        traversal.append(self)
        if self.right:
            traversal += self.right.inorder()
        return traversal


class BinSearchTree:
    def __init__(self):
        self.root = None


    def insert(self, key, data):
        if self.root: # 트리가 존재하면
            self.root.insert(key, data)
        else: # 트리가 존재X - 첫 노드 삽입
            self.root = Node(key, data)


    def inorder(self):
        if self.root: # 트리가 존재하면
            return self.root.inorder()
        else:
            return []


BTree = BinSearchTree()

BTree.insert(9, 'd1')
BTree.insert(15, 'd2')
BTree.insert(2, 'd3')
BTree.insert(1, 'd4')
BTree.insert(7, 'd5')
BTree.insert(11, 'd6')

for node in BTree.inorder():
    print(node.key, end=' ')
print()

BTree.insert(8, 'new')
for node in BTree.inorder():
    print(node.key, end=' ')