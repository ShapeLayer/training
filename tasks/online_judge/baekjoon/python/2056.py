from sys import stdin
from collections import deque
input = stdin.readline

def compute(n: int, costs: list[int], _next: list[list[int]]):
    indegree = [0 for _i in range(n + 1)]
    for each in _next:
        for to in each:
            indegree[to] += 1
    q = deque()
    dp = [0 for _i in range(n + 1)]
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i,)
            dp[i] = costs[i]
    while q:
        now = q.popleft()
        for each in _next[now]:
            indegree[each] -= 1
            dp[each] = max(dp[now] + costs[each], dp[each])
            if indegree[each] == 0:
                q.append(each)
    return max(dp)

if __name__ == '__main__':
    n: int = int(input())
    costs: list[int] = [0 for _i in range(n + 1)]
    _next: list[list[int]] = [[] for _i in range(n + 1)]
    for i in range(1, n + 1):
        gets = [*map(int, input().split())]
        costs[i] = gets[0]
        for each in gets[2:]:
            _next[each].append(i)
    print(compute(n, costs, _next))
