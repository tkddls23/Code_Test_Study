# 정렬

- `sorted(list)`: built-in function, returns sorted list
- `.sort()`: list method, changes the list

### option

- `reverse=false`: 오름차순
- `key=lambda variable: expression(variable)`: 정렬 기준 추가

# 탐색

- 선형 탐색(Linear search): 순차적, O(n)
- 이진 탐색(Binary search):

대상 리스트가 이미 정렬되어 있을 때 중간값을 이용하여 탐색 범위를 줄여나감, O(log n)

```python
lower = 0
upper = len(L) - 1
index = -1

while upper >= lower:
    middle = (lower + upper) // 2

    if L[middle] == target:
        index = middle
        break
    elif L[middle] < target:
        lower = middle + 1
    else:
        upper = middle - 1
```
