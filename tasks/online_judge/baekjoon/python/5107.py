from sys import stdin
input = stdin.readline

def compute(n: int, gets: list[int]):
    parents = [i for i in range(n)]
    name = {}
    id_peek = 0
    
    def find(n: int) -> int:
        if parents[n] == n:
            return n
        parents[n] = find(parents[n])
        return parents[n]
    
    def merge(a: int, b: int):
        pa, pb = find(a), find(b)
        if pa > pb:
            parents[pa] = pb
            parents[a] = pb
        else:
            parents[pb] = pa
            parents[b] = pa
    
    cycles = 0
    for _from, _to in gets:
        if _from not in name:
            name[_from] = id_peek
            id_peek += 1
        if _to not in name:
            name[_to] = id_peek
            id_peek += 1
        a, b = name[_from], name[_to]
        if find(a) == find(b):
            cycles += 1
        else:
            merge(a, b)
    return cycles

if __name__ == '__main__':
    i = 1
    while True:
        n = int(input())
        if n == 0:
            break
        gets = [input().split() for _i in range(n)]
        print(i, compute(n, gets))
        i += 1
