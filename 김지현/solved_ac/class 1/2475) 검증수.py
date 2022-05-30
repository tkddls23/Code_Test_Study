list_squares = list(map(lambda x: int(x)**2, input().split()))
print(sum(list_squares) % 10)