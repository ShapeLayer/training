from sys import stdin
input = stdin.readline

class Solve:
    def __init__(self, p: int, w: int, c: int, v: int):
        self.p = p
        self.w = w
        self.c = c
        self.v = v
        self.parents = [i for i in range(p)]
    
    def find(self, n: int) -> int:
        if n == self.parents[n]: return n
        self.parents[n] = self.find(self.parents[n])
        return self.parents[n]

    def merge(self, a: int, b: int):
        pa, pb = self.find(a), self.find(b)
        if pa > pb:
            self.parents[pa] = pb
            self.parents[a] = pb
        else:
            self.parents[pb] = pa
            self.parents[b] = pa

if __name__ == '__main__':
    p, w = map(int, input().split())
    c, v = map(int, input().split())
    solve: Solve = Solve(p, w, c, v)
    width = None
    for s, e, w in sorted([[*map(int, input().split())] for _i in range(w)], key=lambda each: -each[2]):
        solve.merge(s, e)
        if solve.find(c) == solve.find(v):
            width = w
            break
    print(width)
