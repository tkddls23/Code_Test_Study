from string import ascii_lowercase

word = input()
for alphabet in ascii_lowercase:
    print(word.find(alphabet), end=' ')

''' TIL
1. from string import ascii_lowercase
2. string 메소드 .find()는 ValueError가 없음
'''