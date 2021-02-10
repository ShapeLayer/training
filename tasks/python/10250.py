from sys import stdin
from math import ceil
l = int(stdin.readline())

for i in range(l):
    h, w, n = list(map(int, stdin.readline().split()))
    y = n % h
    if y == 0:
        y = h
    x = ceil(n / h)
    print('{}{}'.format(y, str(x).zfill(2)))