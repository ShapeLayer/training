from sys import stdin
input = stdin.readline
INF = int(1e10)

def compute(n: int, adj: list[list[int]]) -> list[list[int]]:
    for k in range(n):
        for i in range(n):
            for j in range(n):
                adj[i][j] = min(adj[i][j], adj[i][k] + adj[k][j])
    return adj

if __name__ == '__main__':
    v, e = map(int, input().split())
    adj = [[INF for _i in range(v)] for _j in range(v)]
    for _i in range(e):
        a, b, c = map(int, input().split())
        adj[a - 1][b - 1] = c  # min(adj[a - 1][b - 1], c)
    adj = compute(v, adj)
    
    _min = INF
    for i in range(v):
        _min = min(_min, adj[i][i])
    print(_min if _min != INF else -1)
