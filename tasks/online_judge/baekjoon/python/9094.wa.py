from sys import stdin
input = stdin.readline

while True:
    n = int(input())
    if n == 0:
        break
    while n > 10:
        _new = 0
        while n:
            _new += n % 10
            n //= 10
        n = _new
    print(n)
