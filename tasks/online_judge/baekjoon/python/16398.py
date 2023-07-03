from sys import stdin
input = stdin.readline

def compute(n: int, cost_map: list[tuple[int]]) -> int:
    parents: list[int] = [i for i in range(n + 1)]

    def find(n: int) -> int:
        if parents[n] == n:
            return n
        parents[n] = find(parents[n])
        return parents[n]

    def merge(a: int, b: int):
        pa, pb = find(a), find(b)
        if pa < pb:
            parents[pb] = pa
            parents[b] = pa
        else:
            parents[pa] = pb
            parents[a] = pb

    conns = [(cost_map[i][j], i, j) for i in range(n) for j in range(i + 1, n)]
    conns.sort()
    total_cost: int = 0
    for each in conns:
        value, a, b = each
        if find(a) != find(b):
            merge(a, b)
            total_cost += value
    return total_cost

if __name__ == '__main__':
    n = int(input())
    cost_map: list[tuple[int]] = [tuple(map(int, input().split())) for _i in range(n)]
    print(compute(n, cost_map))
