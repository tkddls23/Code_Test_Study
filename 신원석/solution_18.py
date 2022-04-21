# 18-1
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
        l = self.left.depth() if self.left else 0 # left의 depth
        r = self.right.depth() if self.right else 0 # right의 depth
        return max(l,r) + 1 # 두 depth중 큰값에 root(= 1)을 더한다


class BinaryTree:

    def __init__(self, r):
        self.root = r

    def size(self):
        if self.root:
            return self.root.size()
        else:
            return 0


    def depth(self):
        if self.root: # root가 있는경우
            return self.root.depth()
        else:
            return 0 # 빈 tree인경우 깊이는 0


def solution(x):
    return 0
