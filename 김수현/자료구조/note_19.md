## 19강 breadth first traversal (이진 트리 - 넓이 우선 순회)

- 원칙

  - 수준(level)이 낮은 노드 우선 방문
  - 같은 수준의 노드 -> 부모 노드 방문 순서에 따라 방문, 왼쪽을 오른쪽보다 먼저 방문
  - 한 노드 방문 -> 나중에 방문할 노드들을 순서대로 기록해 두어야 함 ❗️큐(queue)❗️

- 알고리즘
  1. 초기화(traversal) <- 빈 리스트, q <- 빈 큐
  2. 빈 트리가 아니면, root node를 큐에 추가(enqueue)
  3. q가 비어 있지 않은 동안
     - node <- q에서 원소 추출(dequeue)
     - node 방문
     - node 왼쪽, 오른쪽 자식 (있다면) q에 추가
  4. q가 빈 큐가 되면 모든 노드 방문 완료
