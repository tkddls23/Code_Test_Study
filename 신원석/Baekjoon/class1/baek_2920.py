# 음계
n = input().split()
ascending, descending = sorted(n), sorted(n,reverse=True)
result = 'ascending' if n == ascending else 'descending' if n == descending else 'mixed'
print(result)