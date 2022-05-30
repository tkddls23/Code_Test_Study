# remainders = set()
# for i in range(10):
#     remainders.add(int(input()) % 42)
# print(len(remainders))


remainders = {int(input()) % 42 for i in range(10)}
print(len(remainders))

''' TIL
1. 빈 iterable에 반복적으로 push하는 패턴 -> comprehension
2. 집합 메소드: .add(), .update([]), .remove()
'''