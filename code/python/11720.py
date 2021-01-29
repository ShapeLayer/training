from sys import stdin

n = int(stdin.readline())
ns = stdin.readline().rstrip()
r = 0

for i in range(n):
    r += int(ns[i])

print(r)