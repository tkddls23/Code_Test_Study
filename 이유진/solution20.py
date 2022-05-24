* solution.py *

class Node:

    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None


    def insert(self, key, data):
        if key<self.key: #작을 때
            if self.left: #left 노드가 존재할 때
                self.left.insert(key,data)
                
            else: #안할때
                self.left = Node(key, data)
            
        elif key>self.key: #클 때
            if self.right: #right 노드가 존재할 때
                self.right.insert(key,data)
            else: #안할 때
                self.right = Node(key, data)
            
        else: #중복일 때
            raise KeyError


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
        if self.root:
            self.root.insert(key, data)
        else:
            self.root = Node(key, data)


    def inorder(self):
        if self.root:
            return self.root.inorder()
        else:
            return []


def solution(x):
    return 0