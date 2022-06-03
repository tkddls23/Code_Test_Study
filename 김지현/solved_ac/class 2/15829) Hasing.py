def get_id(alphabet):
    return ord(alphabet) - 96

l = int(input())
s = input()
sum = 0

for i in range(len(s)):
    sum += get_id(s[i]) * 31**i
print(sum % 1234567891)