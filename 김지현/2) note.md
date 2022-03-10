- 배열: 원소들을 순서대로 늘어놓은 것

# O(1)

- 자료 수와 관계 없이 일정한 실행 시간을 갖는 알고리즘 = 상수 시간 소요
  - 마지막에 원소 추가: `.append(element)`
  - 마지막 원소 삭제: `.pop()` that returns `last_element`

# O(n)

- 자료 수에 비례하는 실행 시간을 갖는 알고리즘 = 선형 시간 소요
  - 중간에 원소 삽입: `.insert(index, element)`
  - 중간 원소 삭제: `.pop(index)`, `del(list[index])`
  - 원소 인덱스 찾기: `.index(element)`
