# A+B-3
case = []
while True:
    try:
        test = list(map(int, input().split()))
        case.append(test[0]+test[1])
    except:
        break
    
for i in case:
    print(i)