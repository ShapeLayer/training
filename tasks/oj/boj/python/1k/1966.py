from sys import stdin
puts = stdin.readline

for _ in range(int(puts())):
    n, m = map(int, puts().split())
    # n = length, m = watchdog target
    q = list(map(int, puts().split()))
    while True:
        i = q.pop(0)
        if i >= max(q):
            if m == 0:
                break
            else:
                m -= 1
        else:
            q += [i]

print(m)