# n, zone = int(input()), 1

# while True:
#     if n <= 3*zone*(zone-1) + 1:
#         print(zone)
#         break
#     zone += 1


n = int(input())
total_rooms = zone = 1

while n > total_rooms:
    total_rooms += 6*zone
    zone += 1
print(zone)

''' TIL
직접 수열 식으로 계산하기보다 누적 변수 만들기
'''