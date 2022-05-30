year = int(input())

if year % 4:
    print(0)

else:
    if (year % 100) or (not year % 400):
        print(1)
    else:
        print(0)