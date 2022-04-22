class MaxHeap:

    def __init__(self):
        self.data = [None]

    def insert(self, item):
        self.data.append(item)
        child = self.data.index(item)
        parent = child // 2
        # 삽입한 값이 root값이 아니고 parent값이 child값보다 작은경우 반복
        while child != 1 and self.data[parent] < self.data[child]:
            self.data[parent], self.data[child] = self.data[child], self.data[parent]
            child = self.data.index(item)
            parent = child // 2


def solution(x):
    return 0
