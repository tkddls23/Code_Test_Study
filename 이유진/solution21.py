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
            raise KeyError('Key %s already exists.' % key)


    def lookup(self, key, parent=None):
        if key < self.key:
            if self.left:
                return self.left.lookup(key, self)
            else:
                return None, None
        elif key > self.key:
            if self.right:
                return self.right.lookup(key, self)
            else:
                return None, None
        else:
            return self, parent


    def inorder(self):
        traversal = []
        if self.left:
            traversal += self.left.inorder()
        traversal.append(self)
        if self.right:
            traversal += self.right.inorder()
        return traversal


    def countChildren(self):
        count = 0
        if self.left:
            count += 1
        if self.right:
            count += 1
        return count


class BinSearchTree:

    def __init__(self):
        self.root = None


    def insert(self, key, data):
        if self.root:
            self.root.insert(key, data)
        else:
            self.root = Node(key, data)


    def lookup(self, key):
        if self.root:
            return self.root.lookup(key)
        else:
            return None, None


    def remove(self, key):
        node, parent = self.lookup(key)
        if node:
            nChildren = node.countChildren()
            # The simplest case of no children
            if nChildren == 0:
                
                if parent: # 만약 parent 가 있으면
                    if node == parent.left: # node 가 왼쪽 자식인지 오른쪽 자식인지 판단하여
                        parent.left=None # parent.left 또는 parent.right 를 None 으로 하여

                    if node == parent.right: # node 가 왼쪽 자식인지 오른쪽 자식인지 판단하여
                        parent.right=None # parent.left 또는 parent.right 를 None 으로 하여
                
                else: # 만약 parent 가 없으면 (node 는 root 인 경우)
                    self.root=None # self.root 를 None 으로 하여 빈 트리로 만듭니다.
                    
            # When the node has only one child
            elif nChildren == 1:
                
                if node.left: # 하나 있는 자식이 왼쪽인지 오른쪽인지를 판단하여
                    i = node.left # 그 자식을 어떤 변수가 가리키도록 합니다.
                else:
                    i = node.right # 그 자식을 어떤 변수가 가리키도록 합니다.
                
                if parent: # 만약 parent 가 있으면
                    if node == parent.left: # node 가 왼쪽 자식인지 오른쪽 자식인지 판단하여
                        parent.left=i # 위에서 가리킨 자식을 대신 node 의 자리에 넣습니다.
                        
                    if node == parent.right: # node 가 왼쪽 자식인지 오른쪽 자식인지 판단하여
                        parent.right=i # 위에서 가리킨 자식을 대신 node 의 자리에 넣습니다.
                
                
                else: # 만약 parent 가 없으면 (node 는 root 인 경우)
                    self.root = i # self.root 에 위에서 가리킨 자식을 대신 넣습니다.
                
                
            # When the node has both left and right children
            else:
                parent = node # parent 는 node 를 가리키고 있고,
                successor = node.right # successor 는 node 의 오른쪽 자식을 가리키고 있으므로
                
                
                # successor 로부터 왼쪽 자식의 링크를 반복하여 따라감으로써
                # 순환문이 종료할 때 successor 는 바로 다음 키를 가진 노드를,
                # 그리고 parent 는 그 노드의 부모 노드를 가리키도록 찾아냅니다.
                while successor.left:
                    parent = successor
                    successor = successor.left
                
                
                # 삭제하려는 노드인 node 에 successor 의 key 와 data 를 대입합니다.
                node.key = successor.key
                node.data = successor.data
                
                 # 이제, successor 가 parent 의 왼쪽 자식인지 오른쪽 자식인지를 판단하여
                if successor == parent.left:
                    parent.left = successor.right
                    # 그에 따라 parent.left 또는 parent.right 를
                    # successor 가 가지고 있던 (없을 수도 있지만) 자식을 가리키도록 합니다.
                    
                else: # successor가 parent.right 일 때 (삭제되려는 오른쪽 서브트리에서 바로 successor가 발견되는 경우)
                    parent.right=successor.right
                    

            return True

        else:
            return False


    def inorder(self):
        if self.root:
            return self.root.inorder()
        else:
            return []


def solution(x):
    return 0