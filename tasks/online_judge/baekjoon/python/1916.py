import heapq
from sys import stdin
input = stdin.readline

INF = int(1e10)

n = int(input())
m = int(input())
conns: list[list[tuple[int]]] = [[] for _i in range(n + 1)]
costs: list[int] = [INF for _i in range(n + 1)]
q = []

for _i in range(m):
    f, t, c = map(int, input().split())
    conns[f].append((t, c))
src, dst = map(int, input().split())

heapq.heappush(q, (0, src))
costs[src] = 0

while q:
    cost, now = heapq.heappop(q)
    if cost > costs[now]:
        continue
    for _to, _cost in conns[now]:
        if costs[_to] > costs[now] + _cost:
            costs[_to] = costs[now] + _cost
            heapq.heappush(q, (costs[_to], _to))

print(costs[dst])
