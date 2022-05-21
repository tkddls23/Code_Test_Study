# 1
def f(x):
    return 1 if 0 <= x <= 1 else x * f(x-1)

n, m = map(int, input().split())

if 5 <= n <= 100 and 5 <= m <= 100 and m <= n:
    print(f(n) // (f(n-m) * f(m)))


# 2
from math import factorial as f

n, m = map(int, input().split())

if 5 <= n <= 100 and 5 <= m <= 100 and m <= n:
    print(f(n) // (f(n-m) * f(m)))

''' TIL
1. 소수 계산 시 부동소수점 문제가 발생함
2. math 모듈에 factorial 함수가 존재함
'''