# 22강 힙 - MaxHeap에 원소 삽입하는 메소드 구현
# MaxHeap의 루트노드 값은 가장 큰 값이 된다.

# 힙은 완전 이진 트리 이므로, 노드의 삽입/삭제는 마지막 노드에서 한다.
# [참고] 파이썬의 swap방법 a, b = b, a

class MaxHeap:
    def __init__(self):
        self.data = [None] # len(self.data) == 1


    def insert(self, item):
        self.data.append(item) # 마지막 노드에 삽입

        #idx = len(self.data) - 1
        idx = self.data.index(item) ### index()를 활용하자!!
        pIdx = idx // 2

        while pIdx != 0:
            if item > self.data[pIdx]: # 부모 노드 값보다 클 경우
                self.data[pIdx], self.data[idx] = self.data[idx], self.data[pIdx] # 부모와 swap
                idx = pIdx
                pIdx = idx // 2
            else:
                break


heap = MaxHeap()
heap.insert(20)
heap.insert(6)
heap.insert(12)
heap.insert(2)
heap.insert(4)
print(heap.data)

heap.insert(30)
print(heap.data)
