from collections import deque
from sys import stdin
input = stdin.readline

def compute(n: int, q: int, parents: list[int], queries: list[tuple[int]]) -> list[str]:
    result: list[str] = []
    curr_parents = [i for i in range(n + 1)]
    queries = deque(queries)
    def find(n: int) -> int:
        if curr_parents[n] == n:
            return n
        p = find(curr_parents[n])
        curr_parents[n] = p
        return p
    def merge(a: int, b: int):
        pa, pb = find(a), find(b)
        if pa < pb:
            curr_parents[b] = pa
            curr_parents[pb] = pa
        else:
            curr_parents[a] = pb
            curr_parents[pa] = pb
    while queries:
        query = queries.pop()
        if query[0] == 0:
            # remove oper
            conn_target = query[1]
            merge(conn_target, parents[conn_target])
        else:
            # query oper
            c, d = query[1], query[2]
            result.append('YES' if find(c) == find(d) else 'NO')
    return result

if __name__ == '__main__':
    n, q = map(int, input().split())
    parents: list[int] = [0, 1] + [int(input()) for i in range(n - 1)]
    queries: list[tuple[int]] = [tuple(map(int, input().split())) for _i in range(n - 1 + q)]
    result = compute(n, q, parents, queries)
    print('\n'.join(result[::-1]))
