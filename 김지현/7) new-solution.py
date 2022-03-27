def traverse(self):
    data = []

    curr = self.head
    while curr:
        data.append(curr.data)
        curr = curr.next

    return data