from sys import stdin
input = stdin.readline

MAX: int = int(1e10)

def compute(n: int, m: int, s: int, e: int, conns: list[tuple[int]]):
    is_conn: list[list[int]] = [[-1 for _i in range(n + 1)] for _j in range(n + 1)]
    parents = [i for i in range(n + 1)]

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
            parents[a] = b

    def find_path_value(prev: int, _from: int, _to: int, min_cost: int) -> int:
        if is_conn[_from][_to] != -1:
            min_cost = min(min_cost, is_conn[_from][_to])
        if _from == _to:
            return min_cost
        for i in range(1, n + 1):
            if is_conn[_from][i] != -1 and prev != i:
                query: int = find_path_value(_from, i, _to, min_cost)
                if query != MAX:
                    min_cost = min(min_cost, query)
        return min_cost

    conns.sort(key=lambda each: -each[2])
    for each in conns:
        h1, h2, k = each
        if find(h1) != find(h2):
            merge(h1, h2)
            is_conn[h1][h2], is_conn[h2][h1] = k, k
    
    return find_path_value(-1, s, e, MAX)

if __name__ == '__main__':
    n, m = map(int, input().split())
    s, e = map(int, input().split())
    conns: list[tuple[int]] = [tuple(map(int, input().split())) for _i in range(m)]
    print(compute(n, m, s, e, conns))
