from sys import stdin
from math import ceil
input = stdin.readline

for _i in range(int(input())):
    a, n = map(int, input().split())
    buf = []

    while a:
        buf.append(a % n)
        a //= n

    is_pal = True
    for i in range(ceil(len(buf) / 2)):
        if buf[i] != buf[-(i + 1)]:
            is_pal = False
            break
    print(int(is_pal))
