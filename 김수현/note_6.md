## 6강 Complexity of Algorithms (알고리즘의 복잡도)

- 시간 복잡도(Time Complexity) : 문제의 크기와 이를 해결하는 데 걸리는 시간 사이의 관계
- 공간 복잡도 (Space Complexity) : 문제의 크기와 이를 해결하는 데 필요한 메모리 공간 사이의 관계

- 평균 시간 복잡도(Average Time Complexity) : 임의의 입력 패턴을 가정했을 때 소요되는 시간의 평균
- 최악 시간 복잡도 (Worst-case Time Complexity) : 가장 긴 시간을 소요하게 만드는 입력에 따라 소요되는 시간

- Big-O Notation  
    -> 점근 표기법(asymtotic notation)의 하나  
    -> 어떤 함수의 증가 양상을 다른 함수와의 비교로 표현(알고리즘 복잡도 표현)  
    -> ex) 입력의 크기가 n일 때, 
        O(logn)=입력의 크기의 로그에 비례하는 시간 소요  
        O(n)=입력의 크기에 비려하는 시간 소요  
        ❗️계수는 그다지 중요하지 않음  
    
- 선형 시간 알고리즘 O(n)  
    -> ex) n개의 무작위로 나열된 수에서 최댓값을 찾기 위해 선형 탐색 알고리즘 적용 - 모든 수를 살펴봐야 함
- 로그 시간 알고리즘 O(logn)  
    -> ex) n개의 크기 순으로 정렬된 수에서 특정 값을 찾기 위해 이진 탐색 알고리즘 적용 
- 이차 시간 알고리즘 O(n^2)  
    -> ex) 삽입 정렬 (insertion sort) - Best case: O(n) / Worst case: O(n^2)

- 보다 나은 복잡도를 가지는 정렬 알고리즘  
    -> ex) 병합 정렬(merge sort) O(nlogn)  
        - 정렬할 데이터를 반씩 나누어 각각 정렬 O(logn)  
        - 정렬된 데이터를 두 묶음씩 한데 합침 O(n)  

- 복잡한 문제 - 배낭 문제 (knapsack problem)