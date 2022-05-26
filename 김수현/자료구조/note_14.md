## 14강 Queues (큐)

- 큐 : 자료를 보관할 수 있는 (선형) 구조
- 스택과의 차이점

  - 인큐(enqueue)연산 : 넣을 때 한쪽 끝에서 밀어넣음
  - 디큐(dequeue)연산 : 꺼낼 때 반대쪽에서 뽑아 꺼냄  
    ==> 선입선출(First-In First-Out)

- 큐의 추상적 자료구조 구현  
   ❗️연산 정의  
   -> size() 현재 큐에 들어 있는 데이터 원소의 수 구함  
   -> isEmpty() 현재 큐가 비어있는지 판단  
   -> enqueue(x) 데이터 원소 x를 큐에 추가  
   -> dequeue() 큐 맨 앞의 데이터 원소 제거(반환)  
   -> peek() 큐 맨 앞의 데이터 원소 반환(제거x)

  1. 배열 이용하여 구현  
     -> size - return len(self.data)  
     -> isEmpty - return self.size() == 0  
     -> enqueue(x) - self.data.append(x)  
     -> dequeue - return self.data.pop(0) ❗️가장 먼저 들어온 원소 리턴 -> 시간복잡도 O(n)  
     -> peek - return self.data[0]
  2. 양방향 연결 리스트 이용하여 구현

- 파이썬 제공 라이브러리 : from pythonds.basic.queue import Queue
