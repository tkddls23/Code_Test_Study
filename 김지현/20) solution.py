class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None

    def insert(self, key, data):
        if key < self.key:
            if self.left:
                self.left.insert(key, data)
            else:
                self.left = Node(key, data)

        elif key > self.key:
            if self.right:
                self.right.insert(key, data)
            else:
                self.right = Node(key, data)

        else:
            raise KeyError('This key already exists')


    def lookup(self, key, parent=None):
        if key < self.key:
            return self.left.lookup(key, self) if self.left else None, None
        elif key == self.key:
            return self, parent
        else:
            return self.right.lookup(key, self) if self.right else None, None

    def inorder(self):
        traversal = []
        if self.left:
            traversal += self.left.inorder()
        traversal.append(self)
        if self.right:
            traversal += self.right.inorder()
        return traversal

    def min(self):
        return self.left.min() if self.left else self


class BinSearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key, data):
        if self.root:
            self.root.insert(key, data)
        else:
            self.root = Node(key, data)

    def lookup(self, key):
        return self.root.lookup(key) if self.root else None, None

    def inorder(self):
        if self.root:
            return self.root.inorder()
        else:
            return []

    def min(self):
        return self.root.min() if self.root else None