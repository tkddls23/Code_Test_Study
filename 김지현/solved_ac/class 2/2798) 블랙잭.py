n, m = map(int, input().split())
cards = list(map(int, input().split()))
length_cards = len(cards)

max_sum = 0
for i in range(length_cards - 2):
    for j in range(i+1, length_cards -1):
        for k in range(j+1, length_cards):
            sum = cards[i]+cards[j]+cards[k]
            if max_sum < sum <= m:
                max_sum = sum

print(max_sum)