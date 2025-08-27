from sys import stdin
from heapq import heappush, heappop
INF = int(1e9)
input = stdin.readline

def compute(V: int, E: int, K: int, conns: list) -> list[int]:
    q = []
    heappush(q, (0, K))
    costs = [INF] * (V + 1)
    costs[K] = 0

    while q:
        cost, now = heappop(q)

        if costs[now] < cost:
            continue

        for next_cost, _next in conns[now]:
            if costs[_next] >= costs[now] + next_cost:
                costs[_next] = costs[now] + next_cost
                heappush(q, (costs[_next], _next))

    return costs

if __name__ == "__main__":
    V, E = map(int, input().split())
    K = int(input())
    conns = [[] for _ in range(V + 1)]
    
    for _i in range(E):
        u, v, w = map(int, input().split())
        conns[u].append((w, v))
    
    for each in compute(V, E, K, conns)[1:]:
        if each == INF:
            print("INF")
        else:
            print(each)
