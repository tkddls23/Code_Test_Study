# 백준 11279번 - 최대 힙

import sys

class MaxHeap:
    def __init__(self):
        self.data = [None] # 배열 인덱스 연산을 위해 데이터는 idx=1부터 넣는다 (idx=0은 비워둠)
        
    def insert(self, item):
        self.data.append(item) # 마지막 원소로 삽입
        idx = len(self.data) - 1
        pidx = idx // 2
        while pidx >= 1:
            if item > self.data[pidx]: # 힙 속성 회복과정
                self.data[idx], self.data[pidx] = self.data[pidx], self.data[idx]
                idx = pidx
                pidx = idx // 2
            else:
                break
    
    def remove(self):
        if len(self.data) == 1: # 빈 배열 이면
            return 0
        else:
            ### Pythontic하게 마지막 원소 추출하기: arr[-1]
            self.data[1], self.data[-1] = self.data[-1], self.data[1] # 마지막 원소와 첫 번째 원소값을 swap
            maxData = self.data.pop() # 가장 큰 값 제거

            # 힙 속성 회복과정
            p = 1
            while len(self.data) > 1:
                left = p * 2
                right = p * 2 + 1
                larger = p ### 포인트
                
                if left <= len(self.data) - 1 and self.data[left] > self.data[larger]:
                    larger = left
                if right <= len(self.data) - 1 and self.data[right] > self.data[larger]:
                    larger = right

                if self.data[p] < self.data[larger]:
                    self.data[p], self.data[larger] = self.data[larger], self.data[p]
                    p = larger # parent idx 값 갱신
                else:
                    break
            
            return maxData


heap = MaxHeap()
N = int(input())
for i in range(N):
    ### sys import 필요
    x = int(sys.stdin.readline()) ### input()을 반복적으로 받을 경우 시간초과 발생 가능!!
    if x == 0:
        print(heap.remove())
    elif x > 0:
        heap.insert(x)