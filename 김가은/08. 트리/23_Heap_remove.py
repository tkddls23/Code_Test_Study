# 23강

class MaxHeap:
    def __init__(self):
        self.data = [None]


    def remove(self): # 가장 큰 값 = 루트노드 값 = self.data[1] 를 삭제 후 반환
        if len(self.data) > 1:
            self.data[1], self.data[-1] = self.data[-1], self.data[1]
            data = self.data.pop(-1)
            self.maxHeapify(1) # 힙 속성 회복
        else: # 빈 힙
            data = None
        return data


    def maxHeapify(self, i):
        # 왼쪽 자식 (left child) 의 인덱스를 계산합니다.
        left = 2 * i
        # 오른쪽 자식 (right child) 의 인덱스를 계산합니다.
        right = 2 * i + 1
        larger = i
        # 왼쪽 자식이 존재하는지, 그리고 왼쪽 자식의 (키) 값이 (무엇보다?) 더 큰지를 판단합니다.
        if (len(self.data) - 1) >= left and self.data[left] > self.data[larger]:
            # 조건이 만족하는 경우, larger 는 왼쪽 자식의 인덱스를 가집니다.
            larger = left
        # 오른쪽 자식이 존재하는지, 그리고 오른쪽 자식의 (키) 값이 (무엇보다?) 더 큰지를 판단합니다.
        if (len(self.data) - 1) >= right and self.data[right] > self.data[larger]:
            # 조건이 만족하는 경우, larger 는 오른쪽 자식의 인덱스를 가집니다.
            larger = right
        if larger != i:
            # 현재 노드 (인덱스 i) 와 최댓값 노드 (왼쪽 아니면 오른쪽 자식) 를 교체합니다.
            self.data[i], self.data[larger] = self.data[larger], self.data[i]
            # 재귀적 호출을 이용하여 최대 힙의 성질을 만족할 때까지 트리를 정리합니다.
            self.maxHeapify(larger)


heap = MaxHeap()
heap.data = [None,20,12,14,8,10,11,12,4,2]
print(heap.data)

heap.remove()
print(heap.data)