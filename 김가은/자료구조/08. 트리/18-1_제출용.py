class Node:
    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None


    def size(self):
        l = self.left.size() if self.left else 0
        r = self.right.size() if self.right else 0
        return l + r + 1


    def depth(self):
        h, lh, rh = 0, 0, 0

        if self.left is None and self.right is None:
            return 1
        else:
            if self.left:
                lh = self.left.depth()
            if self.right:
                rh = self.right.depth()
            h = max(lh, rh)

        return h + 1


class BinaryTree:
    def __init__(self, r):
        self.root = r

    def size(self):
        if self.root:
            return self.root.size()
        else:
            return 0

    def depth(self):
            if self.root:
                return self.root.depth()
            else:
                return 0


def solution(x):
    return 0