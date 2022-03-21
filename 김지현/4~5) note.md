# 재귀

- 하나의 함수에서 자신을 다시 호출하여 작업 수행
- trivial case 필요
- Iterative counterpart 알고리즘 가짐
- O(n)
- might be inefficient but 사람이 생각하는 방식으로 구현 가능

```python
def func(n):
    if n..:
        return ..
    else:
        return expression(func(..))
```

- nCm = `n-1Cm + n-1Cm-1` = `n!/((n-m)!*m!)`

```python
def combination(n, m):
    if n == m or m == 0:
        return 1

    return combination(n-1, m) + combination(n-1, m-1)
```

cf)

```python
from math import factorial as f

def combination(n, m):
    return f(n) / (f(n-m) * f(m))
```
