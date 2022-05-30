# for t in range(int(input())):
#     score = 0
#     circles = input().replace("X", " ").split()
#     for c in circles:
#         score += len(c) * (len(c)+1) / 2
#     print(int(score))


for t in range(int(input())):
    score = 0
    length_circles = map(len, input().split("X"))
    for l in length_circles:
        score += l * (l+1) / 2
    print(int(score))