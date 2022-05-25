# 배열의 최대값, index
list = []
for i in range(9):
    list.append(int(input()))

print(max(list))
print(list.index(max(list))+1)