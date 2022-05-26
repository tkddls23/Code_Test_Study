# 두수 비교하기
a = input().split() # 값 분리

if int(a[0]) > int(a[1]):
    print('>')
elif int(a[0]) <int(a[1]):
    print('<')
else:
    print('==')