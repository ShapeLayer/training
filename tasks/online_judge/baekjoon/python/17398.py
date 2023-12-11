from sys import stdin
input = stdin.readline

def compute(n: int, m: int, q: int, conn: list[list[int]], disconn: list[int]):
    is_later = [False for i in range(m)]
    for each in disconn:
        is_later[each - 1] = True
    parents = [i for i in range(n + 1)]
    counts = [1 for _i in range(n + 1)]

    def find(n: int) -> int:
        if n == parents[n]: return n
        parents[n] = find(parents[n])
        return parents[n]
    
    def merge(a: int, b: int):
        pa, pb = find(a), find(b)
        if pa > pb:
            parents[pa] = pb
            parents[a] = pb
            counts[pb] += counts[pa]
            counts[pa] = 0
        elif pa < pb:
            parents[pb] = pa
            parents[b] = pa
            counts[pa] += counts[pb]
            counts[pb] = 0
    
    for i in range(m):
        if is_later[i]:
            continue
        a, b = conn[i]
        merge(a, b)

    cost = 0
    for i in range(q - 1, -1, -1):
        now = disconn[i] - 1
        a, b = conn[now]
        pa, pb = find(a), find(b)
        if pa != pb:
            cost += counts[pa] * counts[pb]
        merge(a, b)
    
    return cost

if __name__ == '__main__':
    n, m, q = map(int, input().split())
    conn: list[list[int]] = [[*map(int, input().split())] for _i in range(m)]
    disconn: list[int] = [int(input()) for _i in range(q)]
    print(compute(n, m, q, conn, disconn))
