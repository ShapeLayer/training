from sys import stdin, setrecursionlimit
from collections import defaultdict
input = stdin.readline
setrecursionlimit(int(1e6))

def compute(n: int, m: int, opers: list):
    parents = [i for i in range(n + 1)]
    diff = [0 for _i in range(n + 1)]

    def find(n: int) -> int:
        if n == parents[n]:
            return n
        p = find(parents[n])
        diff[n] += diff[parents[n]]
        parents[n] = p
        return parents[n]

    def merge(a: int, b: int, w: int):
        pa, pb = find(a), find(b)
        if pa == pb:
            return
        
        parents[pb] = pa
        diff[pb] = diff[a] - diff[b] + w
    
    buf = []
    for oper in opers:
        if oper[0] == '!':
            a, b, w = oper[1:]
            merge(a, b, w)
        else:
            a, b = oper[1:]
            if find(a) != find(b):
                buf.append('UNKNOWN')
                continue
            buf.append(str(diff[b] - diff[a]))

    return buf

if __name__ == '__main__':
    while True:
        n, m = map(int, input().split())
        if n == m == 0:
            break
        opers = []
        for _i in range(m):
            gets = input().split()
            opers.append([gets[0], *map(int, gets[1:])])
        print('\n'.join(compute(n, m, opers)))
