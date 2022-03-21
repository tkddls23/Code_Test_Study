재귀 알고리즘 - 기초

재귀함수 : 자신을 다시 호출하여 작업 수행
ex. 이진트리, 자연수의 합 구하기

def sum(n):
    return n+sum(n-1)

-> 에러 발생

def sum(n):
    if n<=1:
        return n
    
    else:
        return n+sum(n-1)

*재귀호출의 종결조건

재귀 알고리즘의 효율
recursive version VS Iterative Version
O(n) n에 비례하는 복잡도를 가짐

+추가예제
n!을 구하는 재귀함수
def what(n):
    if n<=1:
        return 1

    else:
        return n*what(n-1)