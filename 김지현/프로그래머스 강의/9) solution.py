def popAfter(self, prev):
    # if prev == self.tail: # popAt에서 호출 시에는 always skip
    #     return None

    curr = prev.next
    nextNode = curr.next
    prev.next = nextNode # prev 노드와 next 노드를 연결

    '''
    길이가 1인 리스트의 1번째 원소를 삭제하면, 빈 리스트가 되는데
    self.tail = prev를 실행한다면 tail이 Node(None)으로 존재하게 됨
    따라서 이 경우 None을 할당함
    '''
    if nextNode == None: # 마지막 원소(self.tail)를 삭제하는 경우
        self.tail = prev if prev != self.head else None

    self.nodeCount -= 1
    return curr.data


def popAt(self, pos):
    if pos < 1 or pos > self.nodeCount:
        raise IndexError

    prev = self.getAt(pos - 1)
    return self.popAfter(prev)