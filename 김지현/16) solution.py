class PriorityQueue:
    def __init__(self):
        self.queue = DoublyLinkedList()

    def enqueue(self, x):
        newNode = Node(x)
        curr = self.queue.head

        while curr != self.queue.tail.prev and x < curr.next.data:
            curr = curr.next
        self.queue.insertAfter(curr, newNode)