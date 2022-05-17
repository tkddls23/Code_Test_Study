# 23강

class MaxHeap:
    def __init__(self):
        self.data = [None] # len(self.data) == 1


    def remove(self): # 가장 큰 값 = 루트노드 값 = self.data[1] 를 삭제 후 반환
        if len(self.data) > 1:
            self.data[1], self.data[-1] = self.data[-1], self.data[1]
            data = self.data.pop(-1)
            self.maxHeapify(1) # 힙 속성 회복
        else: # 빈 힙
            data = None
        return data


    def maxHeapify(self, i):
        left = 2 * i # 왼쪽 자식 인덱스
        right = 2 * i + 1 # 오른쪽 자식 인덱스

        larger = i
        # "len(self.data) - 1" = 실제 원소 개수. index 0에 None값을 넣었기 때문에 1 빼줘야 함.
		if left <= (len(self.data) - 1) and self.data[left] > self.data[larger]:
            larger = left
        if right <= (len(self.data) - 1) and self.data[right] > self.data[larger]:
            larger = right
        
		if larger != i: # 비교 후 갱신이 발생했다면
            # 현재 노드 (인덱스 i) 와 최댓값 노드 (왼쪽과 오른쪽 자식 중 큰거) 를 교체합니다.
            self.data[i], self.data[larger] = self.data[larger], self.data[i]
            # 재귀적 호출을 이용하여 최대 힙의 성질을 만족할 때까지 트리를 정리합니다.
            self.maxHeapify(larger)


heap = MaxHeap()
heap.data = [None,20,12,14,8,10,11,12,4,2]
print(heap.data)

heap.remove()
print(heap.data)