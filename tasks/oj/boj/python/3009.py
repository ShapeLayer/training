from sys import stdin
from collections import Counter

x, y = [], []
for _ in range(3):
    x_, y_ = list(map(int, stdin.readline().split()))
    x += [x_]
    y += [y_]

xc = Counter(x)
yc = Counter(y)

xr = 0
yr = 0
for x_ in xc:
    if xc[x_] == 1 or xc[x_] == 3:
        xr = x_
for y_ in yc:
    if yc[y_] == 1 or yc[y_] == 3:
        yr = y_

print(xr, yr)