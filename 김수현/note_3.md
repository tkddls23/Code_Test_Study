## 3강 Sorting & Searching (정렬과 탐색)

- 파이썬 리스트의 정렬  
    (1) sorted()  
        내장함수, 정렬된 새로운 리스트를 얻어냄  
    (2) sort()  
        리스트의 method, 해당 리스트 정렬  

    * 정렬순서 반대로  
        L2 = sorted(L, reverse=True)  
        L.sort(reverser=True)  

    * 문자열로 이루어진 리스트 - 사전(알파벳) 순서  

    * 정렬시 키(key) 지정  
        (1) sorted(L, key=lambda x: len(x))  
            --> 문자열 길이 정렬  
        (2) L.sort(key=lambda x:x['score'], reverse=True)  
            --> L = [{'score':83},{'score':90}] 이 리스트를 점수 높은 순으로 정렬  


- 탐색 알고리즘  
    (1) 선형 탐색(Linear Search)  
        --> O(n):리스트 길이에 비례하는 시간 소요  
    (2) 이진 탐색(Binary Serach)  
        --> 탐색하려는 리스트가 이미 정렬되어 있는 경우에만 적용 가능  
        --> 크기 순으로 정렬되어 있다는 성질 이용  
        --> O(log n):한 번 비교가 일어날 때마다 리스트 반씩 줄임  
    
