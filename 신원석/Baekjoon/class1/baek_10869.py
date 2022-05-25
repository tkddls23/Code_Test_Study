# 사칙연산

n = list(map(int,input().split()))
cal = ['+','-','*','//','%']
for i in cal:
    print(eval(f'{n[0]}{i}{n[1]}'))