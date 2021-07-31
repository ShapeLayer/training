from sys import stdin
puts = stdin.readline
n, m = map(int, puts().split())
c = [] # customers
for _ in range(m):
    c += [int(puts())]
c.sort(reverse = True)
p = (0, 0) # possibles
for i in range(min(len(c), n)):
    s = c[i] * (i+1) # sum
    if s > p[1]:
        p = (c[i], s)
print(p[0], p[1])
