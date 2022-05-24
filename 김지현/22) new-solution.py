class MaxHeap:
    def __init__(self):
        self.data = [None]

    def insert(self, item):
        self.data.append(item)
        item_index = len(self.data) - 1
        parent_index = item_index // 2

        while item_index != 1 and item > self.data[parent_index]:
            self.data[item_index], self.data[parent_index] = self.data[parent_index], item
            item_index, parent_index = parent_index, parent_index // 2