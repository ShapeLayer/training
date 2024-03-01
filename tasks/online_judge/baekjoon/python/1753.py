import heapq
from sys import stdin
input = stdin.readline

INF = 1_000_000

v, e = map(int, input().split())
k = int(input())

conn = [[] for i in range(v + 1)]
costs = [INF for i in range(v + 1)]
costs[k] = 0
q = []
heapq.heappush(q, (0, k))

for _i in range(e):
    _u, _v, _w = map(int, input().split())
    conn[_u].append((_v, _w))

while q:
    cost, now = heapq.heappop(q)
    if costs[now] < cost:
        continue
    for next, w in conn[now]:
        if costs[next] >= costs[now] + w:
            costs[next] = costs[now] + w
            heapq.heappush(q, (costs[next], next))

for i in range(1, v + 1):
    if costs[i] == INF:
        print('INF')
    else:
        print(costs[i])
