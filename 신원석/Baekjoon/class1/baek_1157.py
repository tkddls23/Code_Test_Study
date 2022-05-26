# 단어공부 - 문자열속 빈도수가 가장높은 문자찾기
import collections

string = input()
str_count = collections.Counter(string.upper()) #문장의 각 단어 빈도수 저장
max_str = str_count.most_common(n=2) # 빈도수 가장큰 두 단어 저장

print('?' if len(max_str)>1 and max_str[0][1] == max_str[1][1] else max_str[0][0]) #문자열이 2개이상인 경우, 빈도수가 가장큰 단어가 두개일 때 처리