from sys import stdin
input = stdin.readline

def compute(m: int, n: int, conns: list[tuple[int]]) -> int:
    parents: list[int] = [i for i in range(m)]
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

    conns.sort(key=lambda each: (each[2]))
    excepted: int = 0 
    for each in conns:
        x, y, z = each
        if find(x) != find(y):
            merge(x, y)
        else:
            excepted += z
    return excepted

if __name__ == '__main__':
    while True:
        m, n = map(int, input().split())
        if m == n == 0:
            break
        conns: list[tuple[int]] = [tuple(map(int, input().split())) for _i in range(n)]
        print(compute(m, n, conns))
