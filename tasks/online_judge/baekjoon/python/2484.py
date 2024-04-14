from sys import stdin
from collections import Counter
input = stdin.readline

n = int(input())
_max = -1
for _i in range(n):
    c = Counter([*map(int, input().split())])
    gets = {}
    for each in c:
        if c[each] not in gets:
            gets[c[each]] = [each]
        else:
            gets[c[each]].append(each)

    if 4 in c.values():
        _max = max(_max, 50_000 + gets.values()[0] * 5_000)
    elif 3 in c.values():
        _max = max(_max, 10_000 + gets[gets.index()])
    elif 2 in c.values():
        if len(set(c.values())) == 1:
            _max = max(_max, 2_000 + gets[2][0] * 500 + gets[2][0] * 500)
        else:
            _max = max(_max, 2_000 + gets[2][0] * 100)
    else:
        _max = max(_max, max(c.keys()) * 100)
    _max = max(_max, )