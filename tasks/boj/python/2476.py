from sys import stdin
from collections import Counter
n = int(stdin.readline())
arr = []
for _ in range(n):
    dices = list(map(int, stdin.readline().split()))
    c = Counter(dices)
    k = list(c.keys())
    v = list(c.values())
    if 3 in v:
        arr += [10000 + dices[0]*1000]
    elif 2 in v:
        for i in k:
            if c[i] == 2:
                arr += [1000 + i*100]
    else:
        arr += [max(dices)*100]
print(max(arr))