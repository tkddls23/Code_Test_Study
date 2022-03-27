//10-1

def reverse(self):
        curr = self.tail
        result = []
        
        while curr.prev.prev:
            curr = curr.prev
            result.append(curr.data)
            
        return result

//10-2

def insertBefore(self, next, newNode):
        prev = next.prev
        newNode.next = next
        newNode.prev = prev
        next.prev = newNode
        prev.next = newNode
        self.nodeCount += 1
        
        return True

//10-3

def popAfter(self, prev):
        pop = prev.next
        prev.next = pop.next
        pop.next.prev = prev
        self.nodeCount -= 1
        return pop.data

    def popBefore(self, next):
        pop = next.prev
        next.prev = pop.prev
        pop.prev.next = next
        self.nodeCount -= 1
        return pop.data


    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            raise IndexError
            
        node = self.getAt(pos)
        
        return self.popAfter(node.prev)

//10-4

def concat(self, L):
        if L.nodeCount == 0:
            return True
        
        else:
            self.tail.prev.next = L.head.next
            L.head.next.prev = self.tail.prev
            self.tail = L.tail
            
            self.nodeCount += L.nodeCount
            
        return True