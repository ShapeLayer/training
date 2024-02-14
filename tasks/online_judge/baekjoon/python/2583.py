from collections import deque
from sys import stdin
input = stdin.readline

m, n, k = map(int, input().split())
is_filled = [[False for _i in range(n)] for _j in range(m)]
for each in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    x1, x2 = min(x1, x2), max(x1, x2)
    y1, y2 = min(y1, y2), max(y1, y2)
    for i in range(y1, y2):
        for j in range(x1, x2):
            if not is_filled[i][j]:
                is_filled[i][j] = True

sizes = []
for i in range(m):
    for j in range(n):
        if is_filled[i][j]:
            continue
        q = deque()
        q.append((i, j))
        is_filled[i][j] = True
        size = 1
        while q:
            y, x = q.popleft()
            for dy, dx in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                ny, nx = y + dy, x + dx
                if ny < 0 or ny >= m or nx < 0 or nx >= n:
                    continue
                if not is_filled[ny][nx]:
                    size += 1
                    is_filled[ny][nx] = True
                    q.append((ny, nx))
        sizes.append(size)

print(len(sizes))
print(*sorted(sizes))
