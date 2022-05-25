# 상수
n = input().split()
A,B = list(n[0]),list(n[1])
a_reverse,b_reverse = '', '' #거꾸로 된 문자열

for i in range(len(A)):
    a_reverse += A.pop()

for i in range(len(B)):
    b_reverse += B.pop()

a_reverse,b_reverse = int(a_reverse),int(b_reverse)

if a_reverse > b_reverse:
    print(a_reverse)
else:
    print(b_reverse)
