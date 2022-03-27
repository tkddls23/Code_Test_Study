## 9강 Linked Lists 3 (연결 리스트 3)

- 연결리스트의 장점 : 삽입과 삭제 유연  

- 변형된 연결리스트 : 맨 앞에 dummy node 추가
    - 인덱스 0 활용 가능
    - insertAfter(prev, newNode) -> tail뒤에 삽입하는 경우 고려
    - insertAt -> insertAfter() 호출하여 이용 가능
    - popAfter(prev) -> prev가 마지막인 경우 고려 + 맨 끝의 node 삭제하는 경우 고려
    - popAt -> popAfter() 호출하여 이용 가능