정렬과 탐색

1)정렬
sorted: 정렬된 새로운 리스트를 얻음 
sorted(L)

sort: 해당 리스트를 정렬
L.sort()

정렬 순서를 반대로: reverset=True

ex1. 문자열 길이 순서대로 정렬 -> key 정렬
sorted(L, key=lambda x:len(x))

ex2. 이름순 정렬
L.sort(key=lambda x:x['name'])

2)선형탐색
리스트 길이에 비례하는 시간이 소요 O(n)
리스트에 존재하지 않는 원소를 찾을 때, 맨 끝에 있는 원소를 찾을 때 비효율적

3)이진탐색

*이미 정렬되어 있는 경우에만 적용가능 (크기순 정렬)

lower, upper, middle
(lower+upper)//2=middle -> 한번의 비교가 일어날 때마다 리스트가 절반 O(log n)

*성능비교
자료의 양이 많아질 때 효율적인 알고리즘의 차이 파악
n에 비례하는 순차 탐색 알고리즘 VS 이진 탐색
-> 이진 탐색은 빠르긴 하지만, 정렬되어 있어야 하므로 항상 이진탐색이 답은 아니다.