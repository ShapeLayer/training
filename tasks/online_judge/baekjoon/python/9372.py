from sys import stdin
input = stdin.readline

def compute(n: int, m: int, conn: list[list[bool]]):
    parent = [i for i in range(n + 1)]
    
    def find(n: int) -> int:
        if n == parent[n]:
            return n
        parent[n] = find(parent[n])
        return parent[n]
    
    def merge(a: int, b: int):
        pa, pb = find(a), find(b)
        if pa > pb:
            parent[pa] = pb
            parent[a] = pb
        elif pa < pb:
            parent[pb] = pa
            parent[b] = pa
    
    count = 0
    for a, b in conn:
        if find(a) != find(b):
            merge(a, b)
            count += 1
    return count

for _i in range(int(input())):
    n, m = map(int, input().split())
    conn = [[*map(int, input().split())] for _j in range(m)]
    print(compute(n, m, conn))
