from sys import stdin
input = stdin.readline

class Solution:
    def __init__(self, title: dict):
        self.title = title
        self.range = sorted(title.keys())
        self.l = 0
        self.r = len(self.range) - 1
    
    def query(self, n: int):
        l, r = self.l, self.r
        while l < r:
            m = (l + r) // 2
            if self.range[m] < n:
                l += 1
            elif self.range[m] > n:
                r -= 1
            else:
                return self.title[self.range[m]]
        m = (l + r) // 2
        return self.title[self.range[m]]

if __name__ == '__main__':
    n, m = map(int, input().split())
    title = {}
    for _i in range(n):
        _title, limit = input().split()
        limit = int(limit)
        if limit not in title:
            title[limit] = _title
    solution: Solution = Solution(title)
    for _i in range(m):
        print(solution.query(int(input())))
