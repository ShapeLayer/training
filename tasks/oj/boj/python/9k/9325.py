from sys import stdin
for _ in range(int(stdin.readline())):
    s = int(stdin.readline())
    for __ in range(int(stdin.readline())):
        q, p = map(int, stdin.readline().split())
        s += q * p
    print(s)