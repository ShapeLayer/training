import heapq
from sys import stdin
input = stdin.readline

INF = int(1e10)
n, m = map(int, input().split())

conns: list[list[tuple[int]]] = [[] for _i in range(n + 1)]
costs: list[tuple[int]] = [(INF, None) for _i in range(n + 1)]
q = []

for i in range(m):
    a, b, c = map(int, input().split())
    conns[a].append((b, c, i))
    conns[b].append((a, c, i))

s, t = map(int, input().split())
heapq.heappush(q, (0, s))
costs[s] = (0, None)

while q:
    now_cost, now_node = heapq.heappop(q)
    if now_cost > costs[now_node][0]:
        continue
    for next_node, cost_diff, conn_id in conns[now_node]:
        if costs[next_node][0] > costs[now_node][0] + cost_diff:
            costs[next_node] = (costs[now_node][0] + cost_diff, conn_id)
            heapq.heappush(q, (costs[next_node][0], next_node))

print(costs[t][0])
