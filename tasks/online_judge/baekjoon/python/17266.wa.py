from math import ceil
from sys import stdin
input = stdin.readline

n = int(input())
m = int(input())
pos = sorted([0, n] + [*map(int, input().split())])

mx_len = 0
for i in range(1, m + 2):
    diff = pos[i] - pos[i - 1]
    if i != 1 and i != n - 1:
        diff = diff/2
    mx_len = max(mx_len, diff)
print(ceil(mx_len))
