class LinkedListQueue:
    def __init__(self):
        self.data = DoublyLinkedList()

    def size(self):
        return self.data.getLength()

    def isEmpty(self):
        return not self.data.getLength()

    def enqueue(self, item):
        node = Node(item)
        self.data.insertAt(self.data.getLength()+1, node)

    def dequeue(self):
        return self.data.popAt(1)

    def peek(self):
        return self.data.getAt(1).data