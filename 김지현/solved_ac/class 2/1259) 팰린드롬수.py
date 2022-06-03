# import math

# while True:
#     num = input()
#     if not int(num):
#         break

#     half = math.ceil(len(num) / 2)
#     for i in range(half):
#         if num[i] != num[-i-1]:
#             print("no")
#             break
#     else:
#         print("yes")


while True:
    num = input()
    if not int(num):
        break

    print("yes" if num == num[::-1] else "no")

''' TIL
문자열/리스트 거꾸로: [::-1]
'''