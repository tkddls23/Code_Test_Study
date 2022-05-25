# 알람 시계

n = input().split() # H시 M분
hour = int(n[0])
minute = int(n[1])
minute = minute - 45

if minute >= 0:
    print(f'{hour} {minute}')
elif hour == 0: # 24시간
    print(f'23 {minute+60}')
else:
    print(f'{hour-1} {minute+60}')
