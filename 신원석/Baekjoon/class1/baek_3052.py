# 나머지
test = []
for i in range(10):
    test.append(int(input()) % 42)

test = set(test) # 중복제거
print(len(test))