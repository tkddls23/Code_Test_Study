class Node:
    def countChildren(self):
        count = 0
        if self.left:
            count += 1
        if self.right:
            count += 1
        return count


class BinSearchTree:
    def remove(self, key):
        node, parent = self.lookup(key)
        if node:
            nChildren = node.countChildren()

            # The simplest case of no children
            if nChildren == 0:
                # 만약 parent 가 있으면
                # node 가 왼쪽 자식인지 오른쪽 자식인지 판단하여
                # parent.left 또는 parent.right 를 None 으로 하여
                # leaf node 였던 자식을 트리에서 끊어내어 없앱니다.
                if parent:
                    if parent.left == node:
                        parent.left = None
                    else:
                        parent.right = None
                # 만약 parent 가 없으면 (node 는 root 인 경우)
                # self.root 를 None 으로 하여 빈 트리로 만듭니다.
                else:
                    self.root = None

            # When the node has only one child
            elif nChildren == 1:
                # 하나 있는 자식이 왼쪽인지 오른쪽인지를 판단하여
                # 그 자식을 어떤 변수가 가리키도록 합니다.
                if node.left:
                    child = node.left
                else:
                    child = node.right
                # 만약 parent 가 있으면
                # node 가 왼쪽 자식인지 오른쪽 자식인지 판단하여
                # 위에서 가리킨 자식을 대신 node 의 자리에 넣습니다.
                if parent:
                    if parent.left == node:
                        parent.left = child
                    else:
                        parent.right = child
                # 만약 parent 가 없으면 (node 는 root 인 경우)
                # self.root 에 위에서 가리킨 자식을 대신 넣습니다.
                else:
                    self.root = child

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
                    successor, parent = successor.left, successor
                # 삭제하려는 노드인 node 에 successor 의 key 와 data 를 대입합니다.
                node.key = successor.key
                node.data = successor.data
                # 이제, successor 가 parent 의 왼쪽 자식인지 오른쪽 자식인지를 판단하여
                # 그에 따라 parent.left 또는 parent.right 를
                # successor 가 가지고 있던 (없을 수도 있지만) 자식을 가리키도록 합니다.
                if parent.left == successor:
                    parent.left = successor.right
                else:
                    parent.right = successor.right

            return True

        else:
            return False