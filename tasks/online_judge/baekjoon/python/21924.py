from sys import stdin
input = stdin.readline

def compute(n: int, m: int, conns: list[tuple[int]]):
    parents: list[int] = [i for i in range(n + 1)]

    def find(n: int) -> int:
        if parents[n] == n:
            return n
        parents[n] = find(parents[n])
        return parents[n]

    def merge(a: int, b: int) -> int:
        pa, pb = find(a), find(b)
        if pa < pb:
            parents[pb] = pa
            parents[b] = pa
        else:
            parents[pa] = pb
            parents[a] = pb

    conns.sort(key=lambda each: each[2])
    total_cost: int = 0
    selected_cost: int = 0
    excepted_cost: int = 0
    for each in conns:
        a, b, c = each
        total_cost += c
        if find(a) != find(b):
            merge(a, b)
            selected_cost += c
        else:
            excepted_cost += c

    is_same: int = 0
    for i in range(1, n + 1):
        if parents[i] == i:
            is_same += 1
    if is_same > 1:
        return -1
    return total_cost - selected_cost

if __name__ == '__main__':
    n, m = map(int, input().split())
    conns: list[tuple[int]] = [tuple(map(int, input().split())) for _i in range(m)]
    print(compute(n, m, conns))
