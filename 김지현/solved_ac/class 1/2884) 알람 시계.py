# h, m = map(int, input().split())
# earlier_time = h*60 + m - 45
# if earlier_time < 0:
#     earlier_time += 24*60

# h = earlier_time // 60
# m = earlier_time - 60*h
# print(h, m)


h, m = map(int, input().split())
earlier_time = h*60 + m - 45
print(earlier_time // 60 % 24, earlier_time % 60)