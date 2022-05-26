class MaxHeap:

    def __init__(self):
        self.data = [None]


    def insert(self, item):
        self.data.append(item)
        index = len(self.data) - 1

        while index != 1:
            parent = index//2
            if self.data[index] > self.data[parent]:
                self.data[index], self.data[parent] = self.data[parent], self.data[index]
                index = parent
            else:
                break


def solution(x):
    return 0