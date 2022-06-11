n1, n2 = map(int, input().split())

# 유클리드 호제법

# 2개의 자연수 a, b에 대해서 a를 b로 나눈 나머지를 r이라 하면(단, a > b),
# a와 b의 최대공약수는 b와 r의 최대공약수
# 위 성질에 따라 b를 r로 나눈 나머지 r'를 구하고, 다시 r을 r'로 나눈 나머지를 구하는 과정을 반복하여 
# 나머지가 0이 되었을 때 나누는 수가 a와 b의 최대공약수
def gcd(n1, n2):
    while(n2):
        n1, n2 = n2, n1 % n2
    return n1

# 최소공배수는 a, b의 곱을 a, b의 최대 공약수로 나누면 됨
def lcm(n1, n2):
    return n1 * n2 // gcd(n1, n2)

print(gcd(n1, n2))
print(lcm(n1, n2))

# #두 수 중 작은 수 부터 1까지 -1을 하면서
# for i in range(min(n1,n2),0,-1):
#     if n1%i==0 and n2%i==0:
#         print(i)
#         break

# for i in range(max(n1,n2),(n1*n2)+1):
#     if i%n1==0 and i%n2==0:
#         print(i)
#         break