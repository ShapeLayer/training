from sys import stdin
input = stdin.readline

def compute(n: int, routes: list[tuple[int]]) -> int:
    parents = [i for i in range(n + 1)]
    routes.sort()

    def merge(a: int, b: int):
        pa, pb = find(a), find(b)
        if pa < pb:
            parents[pb] = pa
        else:
            parents[pa] = pb

    def find(n: int) -> int:
        if parents[n] == n:
            return n
        p = find(parents[n])
        parents[n] = p
        return p

    costs = 0
    conns = 0
    for route in routes:
        if conns == n - 2:
            break
        c, a, b = route
        if find(a) != find(b):
            merge(a, b)
            costs += c
            conns += 1

    return costs

if __name__ == '__main__':
    n, m = map(int, input().split())
    routes: list[tuple[int]] = []
    for _i in range(m):
        a, b, c = map(int, input().split())
        routes.append((c, a, b))
    print(compute(n, routes))
