#브루트포스 알고리즘 : 완전탐색, 모든 경우의 수 탐색하면서 요구조건에 충족되는 결과만을 가져옴

target = int(input())

for i in range(1, target+1):
    values = list(map(int, str(i)))
    result = i + sum(values)
    
    if result == target:
        print(i)
        break

    # 반복문을 끝까지 다 돌았을 때(생성자가 없을 때)
    if i == target:
        print(0)