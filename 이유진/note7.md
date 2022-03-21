연결리스트

추상적 자료구조: 데이터 아이템 set들에 가해질 수 있는 일련의 연산을 추상적으로 밖에 보여주는 것

기본적 연결리스트: 앞에 있는 것이 뒤에 있는 것을 가르키도록 데이터들을 늘어 놓음

Node: data, link(next)
Head: 리스트의 맨 앞
Tail: 리스트의 맨 끝
of nodes: 노드의 갯수

-Node Class
Class Node:
    def __init__(self,item):
        self.data=item
        self.next=None

-LinkedList Class
Class LinkedList:
    def __init__(self):
        self.noeCount=0
        self.head=None
        self.tail=None

-연산 정의
1. 특정 원소 참조
2. 리스트순회
3. 길이 얻어내기
4. 원소삽입
5. 원소삭제
6. 두 리스트 합치기

배열 VS 연결리스트
연속한 위치 / 임의의 위치
매우 간편 / 선형탐색과 유사
O(1) / O(n)