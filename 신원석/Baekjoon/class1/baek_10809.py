# 알파벳 찾기
s = input()
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in range(26):
    print(s.find(alphabet[i]), end=' ')

