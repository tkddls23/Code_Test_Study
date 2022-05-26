## 7강 Linked Lists 1 (연결 리스트 1)

- 추상적 자료구조(Abstract Data Structures)  
    - Data -> ex) 정수, 문자열, 레코드 ...
    - A set of operations -> ex) 삽입, 삭제, 순회, 정렬, 탐색 ...

- 기본적 연결 리스트 구조 : 앞에 있는 아이템이 뒤에 있는 아이템을 가리킴  
    -> Node - Data , Link(next)  
    -> Node 내의 데이터는 다른 구조로 이루어질 수 있음(문자열, 레코드, 연결리스트 등)  
    -> Head: 리스트의 처음 요소  
    -> Tail: 리스트의 끝 요소  
    -> # of nodes: 리스트의 노드 개수 기록 필요  

- 자료구조 정의 -> 비어있는 연결리스트   

    class Node:  
        def __init__(self, item):  
            self.data = item  
            self.next = None  
    
    class LinkedList:  
        def __init__(self):  
            self.nodeCount = 0  
            self.head = None  
            self.tail = None  

- 연산 정의  
    1. 특정 원소 참조 (k번째)  
        -> 첫 노드에 index 1 지정(0은 다른 용도로 사용)
    2. 리스트 순회
    3. 길이 걷어내기
    4. 원소 삽입
    5. 원소 삭제
    6. 두 리스트 합치기

- 배열과 연결 리스트 비교  
    ||배열|연결 리스트|
    |저장 공간|연속한 위치|임의의 위치|
    |특정 원소 지칭|매우 간편(O(1))|선형탐색과 유사(O(n))|


    