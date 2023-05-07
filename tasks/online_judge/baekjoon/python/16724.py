from sys import stdin
from collections import Counter
input = stdin.readline

DIR_TO_DT = {
    'U': (-1, 0),
    'D': (1, 0),
    'R': (0, 1),
    'L': (0, -1)
}

def compute(n: int, m: int, table: list[str]):
    parents = [i for i in range(n * m)]

    def merge(a: int, b: int):
        pa, pb = find(a), find(b)
        if pa < pb:
            parents[pb] = pa
            parents[b] = pa
        else:
            parents[pa] = pb
            parents[a] = pb

    def find(n: int) -> int:
        if parents[n] == n:
            return n
        p = find(parents[n])
        parents[n] = p
        return p

    for i in range(n):
        for j in range(m):
            now = table[i][j]
            dy, dx = DIR_TO_DT[now]
            ny, nx = i + dy, j + dx
            if 0 <= ny < n and 0 <= nx < m:
                merge(i * m + j, ny * m + nx)

    for i in range(m * n):
        parents[i] = find(i)

    return dict(Counter(parents)).keys()

if __name__ == '__main__':
    n, m = map(int, input().split())
    table = [input().strip() for _i in range(n)]
    print(len(compute(n, m, table)))
