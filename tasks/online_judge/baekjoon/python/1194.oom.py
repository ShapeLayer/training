from collections import deque
from sys import stdin
input = stdin.readline

class Solution:
    def __init__(self, n: int, m: int, map_: list[str]):
        self.n = n
        self.m = m
        self.map = map_
        self._queue: deque = deque([])
    
    def reset_visited(self):
        self._visited: list[list[bool]] = [[False for _i in range(m)] for _j in range(n)]
    
    def visit_tile(self, visited: int, y: int, x: int) -> int:
        shift = y * self.m + x
        visited |= 1 << shift
        return visited
    
    def tile_is_visited(self, visited: int, y: int, x: int) -> bool:
        shift = y * self.m + x
        return (visited & 1 << shift) == 1 << shift

    def collect_key(self, collected: int, key: str):
        shift = ord(key) - 97
        collected |= 1 << shift
        return collected

    def key_is_collected(self, collected: int, key: str) -> bool:
        shift = ord(key) - 65
        return (collected & 1 << shift) == 1 << shift
    
    def pos_is_in_range(self, y: int, x: int) -> bool:
        return 0 <= x < m and 0 <= y < n

    def invoke_bfs(self, y: int, x: int) -> int:
        visited = self.visit_tile(0b0, y, x)
        self._queue.append((y, x, 0, 0b0, visited))
        return self.bfs()

    def bfs(self) -> int:
        while self._queue:
            now = self._queue.popleft()
            y, x, moves, collected, visited = now

            if self.map[y][x] == '#':
                continue
            if self.map[y][x] == '1':
                return moves
            tile_ord = ord(self.map[y][x])
            if 97 <= tile_ord <= 102:
                collected = self.collect_key(collected, self.map[y][x])
                visited = 0
                visited = self.visit_tile(visited, y, x)
            if 65 <= tile_ord <= 70:
                if not self.key_is_collected(collected, self.map[y][x]):
                    continue
    
            for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ny, nx = y + dy, x + dx
                if not self.pos_is_in_range(ny, nx):
                    continue
                if self.tile_is_visited(visited, ny, nx):
                    continue
                visited = self.visit_tile(visited, y, x)
                self._queue.append((ny, nx, moves + 1, collected, visited))
        return -1
    
    def compute(self) -> int:
        y, x = -1, -1
        for i in range(self.n):
            for j in range(self.m):
                if self.map[i][j] == '0':
                    y, x = i, j
        return self.invoke_bfs(y, x)

if __name__ == '__main__':
    n, m = map(int, input().split())
    map_ = [input().strip() for _i in range(n)]
    solve: Solution = Solution(n, m, map_)
    print(solve.compute())
