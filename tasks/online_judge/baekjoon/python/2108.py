from sys import stdin
from collections import Counter
gets = stdin.readline
arr = []
n = int(gets())
for _ in range(n):
    arr += [int(gets())]
c = dict(Counter(arr))
modeval = max(c.values())
modes = []
mode = 0
for key in c:
    if c[key] == modeval:
        modes += [key]
if len(modes) >= 2:
    mode = sorted(modes)[1]
else:
    mode = modes[0]

print(round(sum(arr)/n))
print(sorted(arr)[len(arr)//2])
print(mode)
print(max(arr) - min(arr))