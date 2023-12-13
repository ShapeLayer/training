from sys import stdin
input = stdin.readline

def compute(n: int, m: int, k: int, c: list[int], conn: list[list[int]]) -> int:
    parents = [i for i in range(n)]
    size = [1 for _i in range(n)]

    def find(n: int) -> int:
        if parents[n] == n: return n
        parents[n] = find(parents[n])
        return parents[n]

    def merge(a: int, b: int):
        pa, pb = find(a), find(b)
        if pa > pb:
            parents[pa] = pb
            parents[a] = pb
            c[pb] += c[pa]
            c[pa] = 0
            size[pb] += size[pa]
            size[pa] = 0
        elif pb > pa:
            parents[pb] = pa
            parents[b] = pa
            c[pa] += c[pb]
            c[pb] = 0
            size[pa] += size[pb]
            size[pb] = 0
    
    for a, b in conn:
        a, b = a - 1, b - 1
        merge(a, b)
    
    groups: list[tuple[int]] = []
    for i in range(n):
        if c[i]:
            groups.append((c[i], size[i]))
    ln = len(groups)
    
    dp = [[0 for _i in range(k)] for _j in range(ln)]
    for i in range(ln):
        for j in range(k):
            candies, scale = groups[i]
            if j - scale < 0:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - scale] + candies)

    return dp[ln - 1][k - 1]

if __name__ == '__main__':
    n, m, k = map(int, input().split())
    c = [*map(int, input().split())]
    friends = [[*map(int, input().split())] for _i in range(m)]
    print(compute(n, m, k, c, friends))
