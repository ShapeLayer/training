from sys import stdin
from collections import Counter
from math import ceil
input = stdin.readline

n = int(input())
arr = Counter([*map(int, input().split())])
if max([*arr.values()]) > ceil(n / 2):
    print('NO')
else:
    print('YES')
