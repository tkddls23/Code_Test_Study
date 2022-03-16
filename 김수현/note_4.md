## 4강 Recursive Algorithms1 (재귀 알고리즘 기초1)

- 재귀 함수(recursive functions): 하나의 함수에서 자신을 다시 호출하여 작업 수행  

    ex1) 이진 트리(binary trees)  

    ex2) 1부터 n까지 자연수의 합 구하기  
        def sum(n):  
            if n <= 1:  
                return n  
            else:  
                return n + sum(n-1)  
    * 재귀함수를 호출할 때는 종결 조건 반드시 필요!  

- 재귀 알고리즘의 효율  
    Recursive version vs Iterative version  
    * 효율성 측면에서 iterative version보다 떨어질 가능성 있음

    
