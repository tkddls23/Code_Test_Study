class Node:

    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None

    def insert(self, key, data):

        if key < self.key:  # 찾으려는 key가 root key보다 작은 경우

            if self.left:  # left가 있는경우
                self.left.insert(key, data)
            else:
                self.left = Node(key, data)  # 삽입

        elif key > self.key:  # 찾으려는 key가 root key보다 큰 경우

            if self.right:  # right가 있는경우
                self.right.insert(key, data)
            else:
                self.right = Node(key, data)  # 삽입

        else:  # 이미 존재하는 key인 경우
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
