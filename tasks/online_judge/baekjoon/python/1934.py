from sys import stdin
from collections import Counter
def get_div(n):
    return [i for i in range(1, n//2+1) if n%i == 0] + [n]
for _ in range(int(stdin.readline())):
    a, b = map(int, stdin.readline().split())
    arc = Counter(get_div(a))
    brc = Counter(get_div(b))
    crc = arc - (arc - brc)
    num = 1
    for i in list(crc):
        num *= i
    print(a * b // i)