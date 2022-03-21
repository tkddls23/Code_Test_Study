'''
nodeCount가 0이 아닐 때
반복문을 통해 모든 node의 data 값을 리스트에 담은 후, 해당 리스트를 반환시킴
반복문은 current node가 self.head일 때부터 self.tail일 때까지 실행됨
'''
def traverse(self):
    data = []
    if self.nodeCount == 0:
        return data

    curr = self.head
    while True:
        data.append(curr.data)
        if curr == self.tail:
            break

        curr = curr.next

    return data