import heapq
from sys import stdin
input = stdin.readline

INF = int(1e10)
n, m = map(int, input().split())

conns: list[list[tuple[int]]] = [[] for _i in range(n + 1)]
costs = [INF for _i in range(n + 1)]
q = []

costs[1] = 0
heapq.heappush(q, (0, 1))

for _i in range(m):
    a, b, c = map(int, input().split())
    conns[a].append((b, c))
    conns[b].append((a, c))

while q:
    now_cost, now_node = heapq.heappop(q)
    if now_cost > costs[now_node]:
        continue
    for next_node, cost_diff in conns[now_node]:
        if costs[next_node] > now_cost + cost_diff:
            costs[next_node] = now_cost + cost_diff
            heapq.heappush(q, (costs[next_node], next_node))

print(costs[n])
