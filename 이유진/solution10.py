###1번
    def reverse(self):
        result = []
        curr = self.tail
        while curr.prev.prev:
            curr=curr.prev
            result.append(curr.data)
        return result

###2번
    def insertBefore(self, next, newNode):
        prev=next.prev
        newNode.prev=prev
        newNode.next=next
        prev.next=newNode
        next.prev=newNode
        self.nodeCount+=1
        return True

###3번

    def popAfter(self, prev):
        curr=prev.next
        next=curr.next
        next.prev=prev
        prev.next=next
        
        self.nodeCount-=1
        return curr.data


    def popBefore(self, next):
        curr=next.prev
        next=curr.next
        next.prev=prev
        prev.next=next
        
        self.nodeCount-=1
        return curr.data


    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            raise IndexError
        
        prev=self.getAt(pos-1)
        return self.popAfter(prev)

        
###4번
    def concat(self, L):
        self.tail.prev.next=L.head.next
        L.head.next.prev=self.tail.prev
        self.tail=L.tail
        self.nodeCount+=L.nodeCount