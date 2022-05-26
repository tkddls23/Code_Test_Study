# 21번 이진탐색트리 - remove(key) 구현

# 삭제하려는 노드가 외부노드면서 root노드라면 (유일한 노드 삭제) -> 트리의 root를 None으로 바꿔야 함
# 삭제하는 노드가 root노드 일 경우 대체하는 자식이 새로운 root가 됨

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


    def lookup(self, key, parent=None): # 찾는 키값을 갖는 노드와 그 부모 노드를 반환
        if key < self.key:
            if self.left:
                return self.left.lookup(key, self)
            else: # 찾는 키 존재X
                return None, None
        elif key > self.key:
            if self.right:
                return self.right.lookup(key, self)
            else: # 찾는 키 존재X
                return None, None
        else: # key == self.key 찾음
            return self, parent


    def inorder(self):
        traversal = []
        if self.left:
            traversal += self.left.inorder()
        traversal.append(self)
        if self.right:
            traversal += self.right.inorder()
        return traversal


    def countChildren(self): # 해당 노드의 자식 개수 (0 or 1 or 2개)
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


    def lookup(self, key): # 찾는 키값을 갖는 노드와 그 부모 노드를 반환
        if self.root:
            return self.root.lookup(key)
        else:
            return None, None


    # 삭제한 경우 True, 해당 키의 노드가 없는 경우 False 반환
    def remove(self, key):
        node, parent = self.lookup(key)
        
        if node:
            nChildren = node.countChildren() # 삭제할 node의 자식 개수 반환 (0 or 1 or 2)
            
            # The simplest case of no children (삭제할 노드가 외부노드)
            if nChildren == 0:
                # 만약 parent 가 있으면
                # node 가 왼쪽 자식인지 오른쪽 자식인지 판단하여
                # parent.left 또는 parent.right 를 None 으로 하여
                # leaf node 였던 자식을 트리에서 끊어내어 없앱니다.
                if parent:
                    if node == parent.left:
                        parent.left = None
                    else:
                        parent.right = None

                # 만약 parent 가 없으면 (삭제할 node가 root 인 경우)
                # self.root 를 None 으로 하여 빈 트리로 만듭니다.
                else:
                    self.root = None # 삭제할 node가 외부노드면서 root 노드, 즉 유일한 노드이므로 빈 트리로 만든다.


            # When the node has only one child
            elif nChildren == 1:
                # 하나 있는 자식이 왼쪽인지 오른쪽인지를 판단하여
                # 그 자식을 어떤 변수가 가리키도록 합니다.
                if node.left:
                    Child = node.left
                else:
                    Child = node.right
                
                # 만약 parent 가 있으면
                # node 가 왼쪽 자식인지 오른쪽 자식인지 판단하여
                # 위에서 가리킨 자식을 대신 node 의 자리에 넣습니다.
                if parent:
                    if node == parent.left:
                        parent.left = Child
                    else:
                        parent.right = Child
                # 만약 parent 가 없으면 (삭제할 node가 root 인 경우)
                # self.root 에 위에서 가리킨 자식을 대신 넣습니다.
                else:
                    self.root = Child


            # When the node has both left and right children
            else:
                parent = node
                successor = node.right
                # parent 는 node 를 가리키고 있고,
                # successor 는 node 의 오른쪽 자식을 가리키고 있으므로
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
                # 그에 따라 parent.left 또는 parent.right 를
                # successor 가 가지고 있던 (없을 수도 있지만) 자식을 가리키도록 합니다.
    # successor는 중위순회에서 삭제할 node의 바로 다음에 방문하게 될 노드    
    # successor는 오른쪽 노드로 이동 뒤, 가장 왼쪽에 위치한 노드이므로 항상 successor.left == None 이다.
    # successor.right는 있을 수도, 없을 수도 있음
                sucChild = successor.right
                if successor == parent.left:
                    parent.left = sucChild
                else:
                    parent.right = sucChild

            return True


        else: # 해당 키를 갖는 노드가 없음 - 삭제 불가
            return False


    def inorder(self):
        if self.root:
            return self.root.inorder()
        else:
            return []


BTree = BinSearchTree()
BTree.insert(9, 'd1')
BTree.insert(15, 'd2')
BTree.insert(2, 'd3')
BTree.insert(1, 'd4')
BTree.insert(11, 'd5')
BTree.insert(7, 'd6')
BTree.insert(5, 'd7')
BTree.insert(8, 'd8')
BTree.insert(3, 'd9')
BTree.insert(4, 'd10')
for node in BTree.inorder():
    print(node.key, end=' ')
print()

BTree.remove(4)
for node in BTree.inorder():
    print(node.key, end=' ')
print()


BTree = BinSearchTree()
BTree.insert(1, 'dd')
BTree.remove(1)
print(BTree.inorder())