from sys import stdin
input = stdin.readline

def gcd(a, b):
    return gcd(b % a, a) if b % a else a

for _i in range(int(input())):
    a, b = map(int, input().split())
    if a > b: a, b = b, a
    d = gcd(a, b)
    m = d * (a // d) * (b // d)
    print(m, d)
