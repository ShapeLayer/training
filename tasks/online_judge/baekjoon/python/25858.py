from sys import stdin
from math import floor
input = stdin.readline

n, d = map(int, input().split())
c = [int(input()) for _i in range(n)]
_sum = sum(c)
for row in [floor(d * (each / _sum)) for each in c]:
    print(row)
