import heapq
from sys import stdin
input = stdin.readline

INF = int(1e10)

n = int(input())
q = []
dt = [(0, 1), (1, 0), (-1, 0), (0, -1)]

_map = [[*map(int, input().split())] for _i in range(n)]
costs: list[list[int]] = [[INF for _i in range(n)] for _j in range(n)]
costs[0][0] = 0
heapq.heappush(q, (0, 0))

while q:
    now_cost, now_node = heapq.heappop(q)
    y, x = now_node // n, now_node % n
    if now_cost > costs[y][x]:
        continue
    for dy, dx in dt:
        ny, nx = y + dy, x + dx
        if not (0 <= ny < n and 0 <= nx < n):
            continue
        cost_diff = max(now_cost, abs(_map[y][x] - _map[ny][nx]))
        if costs[ny][nx] > cost_diff:
            costs[ny][nx] = cost_diff
            heapq.heappush(q, (costs[ny][nx], ny * n + nx))

print(costs[n - 1][n - 1])
