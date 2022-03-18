# Complexity

- 시간 복잡도(Time complexity): 입력의 크기 ↔ 실행에 소요되는 시간
- 공간 복잡도(Space complexity): 입력의 크기 ↔ 실행에 필요한 메모리 공간
- 평균 시간 복잡도(Average time complexity): 임의의 입력 패턴을 가정했을 때 소요되는 시간의 평균
- 최악 시간 복잡도(Worst-case time complexity): 가장 긴 시간을 소요하게 만드는 입력 패턴일 때 소요되는 시간

# Big-O notation

- 알고리즘의 성능(complexity)을 수학적으로 표현
- 어떤 함수의 증가 양상을 다른 함수와의 비교로 표현 → 입력의 크기에 따라 실행 시간이 얼마나 증가하는가

### O(n)

- 선형 시간 알고리즘
- 입력의 크기에 비례하는 시간 소요
- ex) `max()`: average case = worst case = O(n)

### O(log n)

- 로그 시간 알고리즘
  - 입력의 크기의 log에 비례하는 시간 소요
    - 한번 처리할 때마다 검색할 데이터 양이 절반씩 감소
- ex) Binary search

### O(n^2)

- 2차 시간 알고리즘
- ex) Insertion sort(삽입 정렬): best case = O(n), worst case = O(n^2)
  - cf) Merge sort(병합 정렬): O(nlog n) → better
    - 데이터를 반씩 나눔 - log(n)
    - 두 묶음씩 정렬해 나가며 정렬된 묶음들을 서로 합침 - n
