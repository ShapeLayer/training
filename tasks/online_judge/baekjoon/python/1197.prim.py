from sys import stdin
import heapq
input = stdin.readline
INF = int(1e10)

def compute(v: int, conns: list[int]) -> int:
    visited = [False for _ in range(v + 1)]
    hq = []

    result = 0
    now = 1
    visited[now] = True
    for cost, _next in conns[now]:
        heapq.heappush(hq, (cost, _next))
    
    while hq:
        cost, now = heapq.heappop(hq)
        if visited[now]:
            continue
        visited[now] = True

        result += cost
        for cost, _next in conns[now]:
            if visited[_next]:
                continue
            heapq.heappush(hq, (cost, _next))

    return result

if __name__ == '__main__':
    v, e = map(int, input().split())
    conns: [int, list[int]] = {}
    for _ in range(e):
        a, b, c = map(int, input().split())
        if a not in conns:
            conns[a] = [(c, b)]
        else:
            conns[a].append((c, b))
        if b not in conns:
            conns[b] = [(c, a)]
        else:
            conns[b].append((c, a))

    print(compute(v, conns))
