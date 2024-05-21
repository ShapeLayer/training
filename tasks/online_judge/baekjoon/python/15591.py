from sys import stdin
from collections import deque
input = stdin.readline

def compute(n: int, q: int, usado: list[list[int]], query: list[list[int]]):
    conn = [[] for _i in range(n + 1)]
    for p, q, r in usado:
        conn[p].append((q, r))
        conn[q].append((p, r))
    query_result = []
    for k, v in query:
        visits = [False for _i in range(n + 1)]
        q = deque([v])
        visits[v] = True
        counts = 0
        while q:
            now = q.popleft()
            for next_v, next_r in conn[now]:
                if next_r >= k and not visits[next_v]:
                    counts += 1
                    visits[next_v] = True
                    q.append(next_v)
        query_result.append(counts)
    return query_result

if __name__ == '__main__':
    n, q = map(int, input().split())
    usado = [[*map(int, input().split())] for _i in range(n - 1)]
    query = [[*map(int, input().split())] for _i in range(q)]
    for each in compute(n, q, usado, query):
        print(each)
