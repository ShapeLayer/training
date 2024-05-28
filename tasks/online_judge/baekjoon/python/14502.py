from sys import stdin
from collections import deque
input = stdin.readline

dt = ((1, 0), (-1, 0), (0, 1), (0, -1))

class Solution:
    def __init__(self, n: int, m: int, gets: list[list[int]]):
        self.n = n
        self.m = m
        self.gets = gets
        self.virus = []
        self.empty = 0
        for i in range(n):
            for j in range(m):
                if gets[i][j] == 0:
                    self.empty += 1
                elif gets[i][j] == 2:
                    self.virus.append((i, j))
        self.result = -1
    
    def bfs(self):
        empty = self.empty - 3
        q = deque(self.virus)
        _map = [[self.gets[i][j] for j in range(m)] for i in range(n)]
        while q:
            y, x = q.popleft()
            for dy, dx in dt:
                ny, nx = y + dy, x + dx
                if not (0 <= ny < n and 0 <= nx < m):
                    continue
                if _map[ny][nx] != 0:
                    continue
                _map[ny][nx] = 2
                empty -= 1
                q.append((ny, nx))
        self.result = max(self.result, empty)

    def invoke(self, depth):
        if depth == 3:
            self.bfs()
            return

        for i in range(self.n):
            for j in range(self.m):
                if self.gets[i][j] == 0:
                    gets[i][j] = 1
                    self.invoke(depth + 1)
                    gets[i][j] = 0

    def compute(self):
        self.invoke(0)

if __name__ == '__main__':
    n, m = map(int, input().split())
    gets = [[*map(int, input().split())] for _i in range(n)]
    solve = Solution(n, m, gets)
    solve.compute()
    print(solve.result)
