# 잘못된 접근: 분리집합

from sys import stdin
input = stdin.readline

def compute(n, k, conns):
    parents = [i for i in range(n)]
    departs = [False for i in range(n)]
    lands = [False for i in range(n)]
    def find(n: int) -> int:
        if parents[n] != n:
            parents[n] = find(parents[n])
        return parents[n]
    
    def merge(a: int, b: int):
        pa, pb = find(a), find(b)
        if pa > pb:
            parents[pa] = pb
            parents[a] = pb
        elif pa < pb:
            parents[pb] = pa
            parents[b] = pa

    conns.sort(key=lambda each: each[2])
    costs = 0
    for _from, _to, cost in conns:
        if find(_from) != find(_to):
            if departs[_from]:
                continue
            if lands[_to]:
                continue
            merge(_from, _to)
            departs[_from] = True
            lands[_to] = True
            costs += cost
        if len(set(parents)) == 1:
            break
    return costs

if __name__ == '__main__':
    n, k = map(int, input().split())
    conns = [] # (from, to, cost)
    for i in range(n):
        gets = [*map(int, input().split())]
        for j in range(n):
            if i == j:
                continue
            conns.append((i, j, gets[j]))
    print(compute(n, k, conns))
