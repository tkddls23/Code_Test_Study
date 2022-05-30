word = input().lower()
max_count = 0

for alphabet in set(word):
    count = word.count(alphabet)
    if count > max_count:
        max_count = count
        frequent_alphabet = alphabet.upper()
    elif count == max_count:
        frequent_alphabet = "?"

print(frequent_alphabet)

''' TIL
1. for문 내에서 생성한 변수를 전역적으로 접근 가능함
2. 다음 loop으로 넘어가도 해당 변수가 사라지지 않음
'''