# 트리

> Node와 edge를 이용해 데이터 배치 형태를 추상화한 자료구조

- Root node + internal nodes + leaf nodes
- Root node에 가까운 parent node + child nodes

한 Node의 child nodes는 여러 개 가능 but parent node는 한 개

<br>

- 같은 부모를 가진 sibling nodes
- Ancestor nodes + descendant nodes: 모든 나머지 nodes는 root node의 후손

- Node level from 0
- Tree height = Max node level + 1
- Subtree: 한 node 기준으로 밑을 잘라낸 것
- Node degree: 자식(subtree)의 수

Leaf nodes의 degree = 0

# 이진 트리(Binary Tree)

- 모든 노드의 degree가 2 이하인 트리
- 재귀적 정의: 빈 tree 이거나 Root node + left subtree + right subtree

이 때 left subtree와 right subtree도 이진 트리

# 포화 이진 트리(Full Binary Tree)

- 모든 레벨에서 노드들이 모두 채워져 있는 이진 트리
- 높이가 k이고 노드의 개수가 2^k-1인 이진 트리

# 완전 이진 트리(Complete Binary Tree)

- 레벨 k-2 까진 모든 노드가 2개의 자식을 가진 포화 이진 트리
- 레벨 k-1 에서는 왼쪽부터 노드가 순차적으로 채워져 있는 이진 트리
