from sys import stdin
from collections import deque
input = stdin.readline

def compute(n: int, costs: list[int], _next: list[list[int]]):
    indegree = [0 for _i in range(n + 1)]
    built_at = [0 for _i in range(n + 1)]
    for row in _next:
        for each in row:
            indegree[each] += 1
    q = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
            built_at[i] = costs[i]
    while q:
        now = q.popleft()
        for each in _next[now]:
            indegree[each] -= 1
            built_at[each] = max(built_at[each], costs[each] + built_at[now])
            if indegree[each] == 0:
                q.append(each)
    return built_at

if __name__ == '__main__':
    n = int(input())
    costs = [0 for _i in range(n + 1)]
    _next = [[] for _i in range(n + 1)]
    for i in range(1, n + 1):
        gets = [*map(int, input().split())]
        costs[i] = gets[0]
        for j in gets[1:-1]:
            _next[j].append(i)
    built_at = compute(n, costs, _next)
    for each in built_at[1:]:
        print(each)
