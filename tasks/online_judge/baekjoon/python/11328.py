from sys import stdin
from collections import Counter
input = stdin.readline

def strfry(a: str, b: str) -> bool:
    a, b = dict(Counter(a)), dict(Counter(b))
    for _k in [*a.keys()] + [*b.keys()]:
        if _k not in a or _k not in b:
            return False
        if a[_k] != b[_k]:
            return False
    return True

for _i in range(int(input())):
    print('Possible' if strfry(*input().split()) else 'Impossible')
