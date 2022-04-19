## 18강 Binary Trees (이진 트리)

- 이진 트리의 추상적 자료구조; 연산정의

  - size() : 현재 트리에 포함되어 있는 노드의 수
  - depth() : 현재 트리의 깊이(또는 높이)를 구함
  - 순회(traversal)

- 이진 트리의 구현

  - 노드(Node)  
    -> Data  
    -> Left Child  
    -> Right Child

  - 트리(Tree)  
    -> root

  - size()  
    -> 재귀적 방법  
    -> left subtree의 size() + right subtree의 size() + 1(자기자신)

  - depth()  
    -> 재귀적 방법  
    -> left subtree의 depth()와 right subtree의 depth() 중 더 큰 것 + 1

  - Traversal(순회)
    - 깊이 우선 순회(depth first traversal)
      - 중위 순회(in-order traversal) : left subtree -> 자기자신 -> right subtree
      - 전위 순회(pre-order traversal) : 자기자신 -> left subtree -> right subtree
      - 후위 순회(post-order traversal) : left subtree -> right subtree -> 자기자신
    - 넓이 우선 순회(breadth first traversal)
