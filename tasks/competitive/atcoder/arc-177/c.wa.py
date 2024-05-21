from sys import stdin
from collections import defaultdict, deque
input = stdin.readline

MAX = int(1e10)
n = int(input())
gets = [[0 if each == 'R' else 1 for each in input().strip()] for _i in range(n)]

passes = [
    # not changed current, changed current
    [[defaultdict(lambda: [MAX, MAX]) for _i in range(n)] for _j in range(n)],
    [[defaultdict(lambda: [MAX, MAX]) for _i in range(n)] for _j in range(n)]
]

dt = ((0, 1), (0, -1), (1, 0), (-1, 0))

q = deque([(0, 0, 0, 0, 0), (0, n - 1, 1, 0, 0)])
def compute(q):
    while q:
        y, x, p, diff, changes = q.popleft()
        print(y, x, p, diff, changes)
        for dy, dx in dt:
            ny, nx = y + dy, x + dx
            if not (0 <= ny < n and 0 <= nx < n): continue
            if gets[ny][nx] == p:
                if passes[p][ny][nx][changes][0] > diff + 1:
                    passes[p][ny][nx][changes][0] = diff + 1
                    q.append((ny, nx, p, diff + 1, changes))
                    print(y, x, p, ny, nx, changes, diff + 1, passes[p][ny][nx][changes])
            else:
                if passes[p][ny][nx][changes + 1][1] > diff + 1:
                    passes[p][ny][nx][changes + 1][1] = diff + 1
                    q.append((ny, nx, p, diff + 1, changes + 1))
compute(q)
print(dict(passes[0][n - 1][n - 1]))
print(dict(passes[1][0][n - 1]))