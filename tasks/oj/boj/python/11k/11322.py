from sys import stdin
puts = stdin.readline
for _ in range(int(puts())):
    n = 1
    i = int(puts())
    while n % i != 0:
        n *= 10
    print(n)
