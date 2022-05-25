# A+B - 5
case = []
while True:
    test = list(map(int, input().split()))
    if test == [0,0]:
        break
    case.append(test[0]+test[1])

    
for i in case:
    print(i)