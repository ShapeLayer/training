from sys import stdin
from math import ceil
a, b, v = list(map(int, stdin.readline().split()))
if a >= v:
    print(1)
else:
    print(ceil((v-b)/(a-b)))