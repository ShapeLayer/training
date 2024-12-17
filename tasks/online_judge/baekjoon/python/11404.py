from sys import stdin
input = stdin.readline
INF = int(1e10)

def compute(n: int, m: int, adj: list[list[int]]) -> list[list[int]]:
    for k in range(n):
        for i in range(n):
            for j in range(n):
                adj[i][j] = min(adj[i][j], adj[i][k] + adj[k][j])
    return adj

if __name__ == '__main__':
    n, m = int(input()), int(input())
    adj = [[INF for _i in range(n)] for _j in range(n)]
    for i in range(n):
        adj[i][i] = 0
    for _i in range(m):
        a, b, c = map(int, input().split())
        adj[a - 1][b - 1] = min(adj[a - 1][b - 1], c)
    [print(*map(lambda each: each if each != INF else 0, row)) for row in compute(n, m, adj)]
