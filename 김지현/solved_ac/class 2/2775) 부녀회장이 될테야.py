for t in range(int(input())):
    k, n = int(input()), int(input())
    floor, people_downstairs = 0, [i for i in range(1, n+1)]
    
    while floor < k:
        floor += 1
        people_here = [sum(people_downstairs[:i+1]) for i in range(n)]
        people_downstairs = people_here
    print(people_here[-1])