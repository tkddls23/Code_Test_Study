# Complexity

- 시간 복잡도(Time complexity): 입력의 크기 ↔ 실행에 소요되는 시간
- 공간 복잡도(Space complexity): 입력의 크기 ↔ 실행에 필요한 메모리 공간
- 평균 시간 복잡도(Average time complexity): 임의의 입력 패턴을 가정했을 때 소요되는 시간의 평균
- 최악 시간 복잡도(Worst-case time complexity): 가장 긴 시간을 소요하게 만드는 입력 패턴일 때 소요되는 시간

# Big-O notation

- 알고리즘의 성능(complexity)을 상한선을 기준으로 수학적으로 표현 - 기본 연산의 횟수

[빅오 표기법 (big-O notation) 이란](https://noahlogs.tistory.com/27)

<br>

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5d419191-b29d-48c4-b02a-1dc80d8b87ee/Untitled.png)

### O(1)

- 상수 시간 알고리즘
- 입력의 크기에 관계 없이 일정한 시간 소요
- `.append(element)`, `.pop()`, `list[i]`

### O(n)

- 선형 시간 알고리즘
- 입력의 크기에 비례하는 시간 소요
- ex) for문, `max(list)`: average case = worst case = O(n), linear search

### O(log n)

- 로그 시간 알고리즘
  - 입력의 크기의 log에 비례하는 시간 소요
    - 한번 처리할 때마다 데이터 양이 절반씩 감소
- ex) Binary search

### O(n^2)

- 2차 시간 알고리즘
- ex) 이중 for문, Insertion sort(삽입 정렬): best case = Ω(n), worst case = O(n^2)

  - cf) Merge sort(병합 정렬): O(nlog n) → better

    - 데이터를 반씩 나눔
    - 두 묶음끼리 정렬하며 서로 합치는 과정을 반복

    [합병정렬(Merge Sort)](https://ratsgo.github.io/data%20structure&algorithm/2017/10/03/mergesort/)
