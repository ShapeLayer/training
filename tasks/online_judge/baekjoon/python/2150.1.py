# Kosaraju
from sys import stdin, setrecursionlimit
setrecursionlimit(int(2e6))
input = stdin.readline

def compute(v: int, e: int, conn_fw: list[list[int]], conn_rw: list[list[int]]):
    done = [False for _i in range(v + 1)]
    stack, scc = [], []

    def _dfs_fw(v: int):
        done[v] = True
        for each in conn_fw[v]:
            if not done[each]:
                _dfs_fw(each)
        stack.append(v)

    def _dfs_rw(v: int):
        done[v] = True
        scc.append(v)
        for each in conn_rw[v]:
            if not done[each]:
                _dfs_rw(each)
    
    for i in range(1, v + 1):
        if not done[i]:
            _dfs_fw(i)
    done = [False for _i in range(v + 1)]
    res = []
    while stack:
        scc = []
        now = stack.pop()
        if not done[now]:
            _dfs_rw(now)
            res.append(sorted(scc))
    return res

if __name__ == '__main__':
    v, e = map(int, input().split())
    conn_fw, conn_rw = [[] for _i in range(v + 1)], [[] for _i in range(v + 1)]
    for _i in range(e):
        a, b = map(int, input().split())
        conn_fw[a].append(b)
        conn_rw[b].append(a)
    res = compute(v, e, conn_fw, conn_rw)
    print(len(res))
    for each in sorted(res):
        print(*each, -1)
