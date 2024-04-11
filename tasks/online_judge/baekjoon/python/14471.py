from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
counts, holds = 0, []

for _i in range(m):
    a, b = map(int, input().split())
    if a < n:
        holds.append(a)
    else:
        counts += 1

if m - 1 == counts:
    print(0)
else:
    result = 0
    for each in sorted(holds, reverse=True)[:m - 1 - counts]:
        result += n - each
    print(result)
