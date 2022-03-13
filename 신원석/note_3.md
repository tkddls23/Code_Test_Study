# sorted vs sort - default 오름차순

**sorted**는 정렬된 리스트를 반환 <br>
**sort**는 기존 리스트를 정렬

`reverse=True`를 통해 정렬 순서를 반대로 할 수 있다

# 알파벳 순서가 아닌 길이 순서로 정렬시

`sorted(L, key=lambda x: len(x))`로 정렬 가능

# 정렬 방식

1. **선형 탐색 Linear Search**
   - O(n) - 리스트의 길이에 비례하는 시간 소요
   - 리스트의 처음부터 하나씩 비교한다
1. **이진 탐색 Binary Search**
   - O(log n) - 절반으로 나눠가며 비교
   - 리스트가 정렬되어 있는 경우에만 적용 가능
