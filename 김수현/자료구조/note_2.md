## 2강 Linear Arrays(선형배열)

- 배열: 원소들을 순서대로 늘어놓은 것

- 리스트 연산1
(1) 끝에 덧붙이기 : L.append('a')
(2) 끝에서 꺼내기 : L.pop() * 해당 요소는 삭제됨

--> 리스트의 길이와 무관하게 처리 가능(상수시간) : O(1)

- 리스트 연산2
(1) 원소 삽입 : L.insert(3,65) *3번 index에 65 삽입
(2) 원소 삭제 : del(L[2]) *2번 index 원소 삭제

--> 리스트 길이에 비례하여 시간이 걸림(선형시간) : O(n)

