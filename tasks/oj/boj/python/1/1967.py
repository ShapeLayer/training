from sys import stdin, setrecursionlimit
input = stdin.readline
setrecursionlimit(10010)
n = int(input())

# n의 입력 범위가 1부터이므로, 1이 들어가면
# 함수가 사용할 자료들이 제대로 생성되지 않아
# 오류가 발생함
if n == 1:
    print(0)
    exit()

tree = {}

for _i in range(n-1):
    a, b, w = map(int, input().split())
    if a not in tree: tree[a] = []
    if b not in tree: tree[b] = []
    tree[a] += [[b, w]]
    tree[b] += [[a, w]]

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
