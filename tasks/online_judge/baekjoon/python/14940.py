from sys import stdin
from collections import deque
input = stdin.readline

dt = ((1, 0), (-1, 0), (0, 1), (0, -1))

def compute(n: int, m: int, t: int, _map: list[list[int]]):
    result = [[-1 for _i in range(m)] for _j in range(n)]

    q = deque()
    q.append((*t, 0))
    result[t[0]][t[1]] = 0
    while q:
        y, x, step = q.popleft()
        for dy, dx in dt:
            ny, nx = y + dy, x + dx
            if not (0 <= ny < n and 0 <= nx < m):
                continue
            if _map[ny][nx] == 0:
                continue
            if result[ny][nx] == -1:
                result[ny][nx] = step + 1
                q.append((ny, nx, step + 1))

    for i in range(n):
        for j in range(m):
            if _map[i][j] == 0:
                result[i][j] = 0

    return result

if __name__ == '__main__':
    n, m = map(int, input().split())
    t = (-1, -1)
    _map = []
    for i in range(n):
        row = [*map(int, input().split())]
        if 2 in row:
            t = (i, row.index(2))
        _map.append(row)
    for row in compute(n, m, t, _map):
        print(*row)
