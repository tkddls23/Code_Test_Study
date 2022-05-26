def popAt(self, pos):
    if pos < 1 or pos > self.nodeCount: # pos 유효성 검사
        raise IndexError
    
    prev = self.getAt(pos - 1)
    curr = prev.next if prev else self.getAt(pos) # prev가 None이라면 getAt으로 curr 구함

    if pos == 1: # 삭제하려는 Node가 리스트의 첫 번째 원소일 때
        self.head = curr.next
        if self.nodeCount == 1: # 리스트 길이가 1일 때
            self.tail = self.head # self.head == None 이므로

    else: # 삭제하려는 Node가 리스트에서 중간 or 마지막에 있을 때
        if pos == self.nodeCount:
            self.tail = prev
        prev.next = curr.next

    self.nodeCount -= 1
    return curr.data