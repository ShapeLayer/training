from sys import stdin
from collections import Counter
input = stdin.readline

for _t in range(int(input())):
    c = dict(Counter(input().strip()))
    c['_'], c['__'] = 0, 0
    print(sum([c[key] for key in sorted(c, key=lambda each: c[each], reverse=True)[2:]]))
