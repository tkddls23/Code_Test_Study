class MaxHeap:

    def __init__(self):
        self.data = [None]


    def insert(self, item):
        #노드 m 번 기준 -> 왼쪽 자식 2*m 번, 오른쪽 자식 2*m+1번, 부모노드 m//2번
        #노드 번호 매기기
        m = len(self.data)
        
        #트리의 마지막 자리(배열 마지막자리)에 새로운 원소를 임시로 저장
        self.data.append(item)
        
        #부모 노드와 키 값을 비교하여 위로 이동
         
        while(m!=1):
            if self.data[m] > self.data[m//2]: #부모 노드보다 클 경우 
                self.data[m], self.data[m//2] = self.data[m//2], self.data[m] # 둘이 값 바꿈
                m = m//2 #위로 이동 
                
            else: #아닐 경우 종료 
                break


def solution(x):
    return 0