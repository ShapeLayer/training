from sys import stdin, setrecursionlimit
setrecursionlimit(20000)

def compute(n: int, m: int, k: int, a: list[int], relations: list[list[int]]) -> int:
    parents = [i for i in range(n + 1)]
    pool = {i: {i} for i in range(1, n + 1)}

    def find(n: int) -> int:
        if parents[n] == n:
            return n
        return find(parents[n])

    def merge(a: int, b: int):
        pa, pb = find(a), find(b)
        if pa > pb:
            parents[a] = pb
            parents[pa] = pb
            pool[pb] |= pool[pa]
            pool[pa] = set()
        else:
            parents[b] = pa
            parents[pb] = pa
            pool[pa] |= pool[pb]
            pool[pb] = set()
    
    for v, w in relations:
        merge(v, w)
    
    cost = 0
    for each in pool:
        members = pool[each]
        if members:
            cost += min([a[member - 1] for member in members])
    return cost

if __name__ == '__main__':
    n, m, k = map(int, input().split())
    a = [*map(int, input().split())]
    relations = [[*map(int, input().split())] for _i in range(m)]
    cost = compute(n, m, k, a, relations)
    print(cost if cost <= k else 'Oh no')
