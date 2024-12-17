from sys import stdin
input = stdin.readline

def compute(v: int, e: int, conns: list[int]) -> int:
    parents = [i for i in range(v + 1)]

    def find(n: int) -> int:
        if parents[n] == n:
            return n
        parents[n] = find(parents[n])
        return parents[n]
    

    weights = 0

    while conns:
        a, b, c = conns.pop()

        pa, pb = find(a), find(b)
        if pa == pb:
            continue
        if pa < pb:
            parents[pa] = pb
            parents[a] = pb
        else:
            parents[pb] = pa
            parents[b] = pa
            
        weights += c
        
    return weights

if __name__ == '__main__':
    v, e = map(int, input().split())
    conns = [[*map(int, input().split())] for _i in range(e)]
    conns.sort(key=lambda each: each[2], reverse=True)
    print(compute(v, e, conns))
