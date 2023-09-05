from sys import stdin, setrecursionlimit
input = stdin.readline
setrecursionlimit(100000)

class Solution:
    def __init__(self, n: int, q: int):
        self.n = n
        self.q = q
        self.d = [0 for _i in range(n + 1)]
        self.parents = [i for i in range(n + 2)]
    
    def find(self, n: int) -> int:
        if self.parents[n] == n:
            return n
        self.parents[n] = self.find(self.parents[n])
        return self.parents[n]

    def merge(self, a: int, b: int) -> int:
        pa = self.find(a)
        pb = self.find(b)
        if pa < pb:
            self.parents[pa] = pb
            self.parents[a] = pb
        else:
            self.parents[pb] = pa
            self.parents[b] = pa
    
    def invoke_query(self, a: int, b: int, x: int):
        idx = a
        while idx <= b:
            if not self.d[idx]:
                self.d[idx] = x
                self.merge(idx, idx + 1)
                idx += 1
            else:
                idx = self.find(idx)

if __name__ == '__main__':
    n, q = map(int,input().split())
    solve: Solution = Solution(n, q)
    for _i in range(q):
        a, b, x = map(int, input().split())
        solve.invoke_query(a, b, x)
    print(*solve.d[1:])
