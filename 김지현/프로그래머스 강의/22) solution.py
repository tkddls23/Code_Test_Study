class MaxHeap:
    def __init__(self):
        self.data = [None]

    def insert(self, item):
        self.data.append(item)
        if len(self.data) == 2:
            return # 부모 노드가 없으므로
        item_index = len(self.data) - 1
        parent_index = item_index // 2

        while item > self.data[parent_index]:
            self.data[item_index], self.data[parent_index] = self.data[parent_index], item
            if parent_index != 1:
                item_index, parent_index = parent_index, parent_index // 2
            else:
                return # item이 트리의 root node가 된 상태