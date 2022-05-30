# a, b = map(lambda x: int(''.join(reversed(x))), input().split())
# print(a if a > b else b)


nums = map(lambda x: int(x[::-1]), input().split())
print(max(nums))