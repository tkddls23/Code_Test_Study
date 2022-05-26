# 배열형태의 환형 큐 ADT 구현

class CircularQueue:
    def __init__(self, n):
        self.maxCount = n
        self.data = [None] * n  # 크기 n인 리스트 [None, None, ...]으로 초기화
        self.count = 0  # 큐 내의 data 개수를 저장하는 속성 유지
        self.front = -1
        self.rear = -1


    def size(self):
        return self.count

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == self.maxCount


    def enqueue(self, x):
        if self.isFull():
            raise IndexError('Queue full')

        self.rear = (self.rear + 1 + self.maxCount) % self.maxCount
        self.data[self.rear] = x    # rear가 가리키는 곳엔 마지막에 삽입한 data
        self.count += 1


    def dequeue(self):
        if self.isEmpty():
            raise IndexError('Queue empty')

        self.front = (self.front + 1 + self.maxCount) % self.maxCount
        x = self.data[self.front]   # front가 가리키는 곳엔 유효한 data X - 배열에선 덮어쓰면 되니까 굳이 None으로 초기화하지 않음
        self.count -= 1
        return x


    def peek(self):
        if self.isEmpty():
            raise IndexError('Queue empty')
        return self.data[(self.front + 1 + self.maxCount) % self.maxCount]


CQ = CircularQueue(5)   # 최대 개수 인자로 넘기기
CQ.enqueue(1)
CQ.enqueue(2)
CQ.enqueue(3)
CQ.enqueue(4)
CQ.enqueue(5)
print(CQ.data)

print(CQ.peek())

CQ.dequeue()
print(CQ.peek())
CQ.dequeue()
print(CQ.peek())
CQ.enqueue(6)
CQ.enqueue(7)
print(CQ.data)

CQ.dequeue()
CQ.dequeue()
print(CQ.peek())
CQ.dequeue()
CQ.dequeue()
print(CQ.peek())
CQ.dequeue()
print(CQ.peek())
