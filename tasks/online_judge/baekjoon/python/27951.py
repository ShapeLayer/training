# WA

from sys import stdin
from collections import Counter
input = stdin.readline

n = int(input())
hangers = list(map(int, input().split()))
counts = Counter(hangers)
u, d = map(int, input().split())
u_margin, d_margin = max(u - counts[1], 0), max(d - counts[2], 0)

if not u_margin + d_margin == counts[3]:
    print('NO')
    exit()

hangs = []
i2s = {1: 'U', 2: 'D'}
remains = {1: u, 2: d}

for hanger in hangers:
    if hanger == 3:
        if u_margin > 0:
            hangs.append(i2s[1])
            remains[1] -= 1
            u_margin -= 1
        else:
            hangs.append(i2s[2])
            remains[2] -= 1
            d_margin -= 1
    else:
        hangs.append(i2s[hanger])
        remains[hanger] -= 1
print(''.join(hangs))
