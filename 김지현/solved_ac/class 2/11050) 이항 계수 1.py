# from math import factorial as f

n,k = map(int, input().split())
# print(f(n) // (f(k) * f(n-k)))

from math import comb as c
print(c(n,k))

''' TIL
math.comb(n,k)
'''