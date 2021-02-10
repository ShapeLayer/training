from sys import stdin

ns = []
for i in range(10):
    n = int(stdin.readline())
    t = n % 42
    if t not in ns:
        ns += [t]
print(len(ns))