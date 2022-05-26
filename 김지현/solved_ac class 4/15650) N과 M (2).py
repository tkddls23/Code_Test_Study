n, m = map(int, input().split()) # 최대 자연수, 수열 원소 개수
seq = []

def get_sequences(start):
    if len(seq) == m:
        print(' '.join(map(str, seq)))
        return
    
    for i in range(start, n+1):
        seq.append(i)
        get_sequences(i+1)
        seq.pop()

get_sequences(1)