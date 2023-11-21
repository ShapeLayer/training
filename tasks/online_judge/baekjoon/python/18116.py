from sys import setrecursionlimit
from collections import defaultdict
input = iter(open(0).read().split('\n')).__next__
MAX = int(1e6) + 1
setrecursionlimit(MAX)

class Solution:
    def __init__(self):
        self.parents = [i for i in range(MAX)]
        self.robot = defaultdict(lambda: 1)
        self.inform = self._merge

    def _find(self, n: int) -> int:
        if n == self.parents[n]:
            return n
        return self._find(self.parents[n])

    def _merge(self, a: int, b: int):
        pa, pb = self._find(a), self._find(b)
        if pa > pb:
            self.parents[a] = pb
            self.parents[pa] = pb
            self.robot[pb] += self.robot[pa]
            self.robot[pa] = 0
        elif pa < pb:
            self.parents[b] = pa
            self.parents[pb] = pa
            self.robot[pa] += self.robot[pb]
            self.robot[pb] = 0
    
    def query(self, c: int) -> int:
        return self.robot[self._find(c)]

if __name__ == '__main__':
    n = int(input())
    solve: Solution = Solution()
    for _i in range(n):
        gets = input().split()
        if gets[0] == 'I':
            solve.inform(*map(int, gets[1:]))
        else:
            print(solve.query(int(gets[1])))
