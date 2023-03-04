from sys import stdin
input = stdin.readline
n = int(input())
tree = {}
entry = []

for _i in range(n):
    line = list(map(int, input().split()))
    now = line.pop(0)
    if now not in tree: tree[now] = []
    while len(line) != 1:
        f, l = line.pop(0), line.pop(0)
        tree[now] += [[f, l]]
    if len(tree[now]) == 1:
        entry += [now]

def dfs(now: int, before: int, stacked: int) -> list:
    res = [-1, -1]
    if before != -1 and len(tree[now]) == 1: return [now, stacked]
    for forward in tree[now]:
        if forward[0] != before:
            proc = dfs(forward[0], now, stacked + forward[1])
            if proc[1] > res[1]: res = proc
    return res

far = dfs(1, -1, 0)
print(dfs(far[0], -1, 0)[1])

'''
WA: 임의의 점을 잡고 한번만 탐색하면 최선의 값이 안 나올 수 있음
    (어딘가 하나가 비정상적으로 길 수 있으므로)
TO: 트리의 모든 잎을 잡고 다 탐색을 돌리면 (아래와 같이) 시간초과가 남
AC: 임의의 가장 먼 점에서(탐색으로 파악) 다시 한번만 더 탐색

max_res = 0
for point in entry:
    res = dfs(point, -1, 0)
    if max_res < res: max_res = res
print(max_res)
'''