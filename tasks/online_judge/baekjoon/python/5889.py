from sys import stdin
from collections import deque
input = stdin.readline

DT = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def compute(n: int, m: int, table: list[str]) -> int:
    visited: list[list[bool]] = [] # init later
    def is_movable(y: int, x: int) -> bool:
        return 0 <= y < n and 0 <= x < m and \
            not visited[y][x] and \
            table[y][x] == 'L'

    def explore(y: int, x: int, moves: int) -> int:
        q = deque([(y, x, 0)])
        res = -1
        visited[y][x] = True
        while q:
            y, x, moves = q.popleft()
            if res < moves:
                res = moves
            for dy, dx in DT:
                ny, nx = y + dy, x + dx
                if is_movable(ny, nx):
                    q.append((ny, nx, moves + 1))
                    visited[ny][nx] = True
        return res

    res = -1
    for y in range(n):
        for x in range(m):
            if table[y][x] == 'L':
                visited = [[False for _i in range(m)] for _j in range(n)]
                res = max(res, explore(y, x, 0))
    return res

if __name__ == '__main__':
    n, m = map(int, input().split())
    table: list[str] = [input().strip() for _i in range(n)]
    print(compute(n, m, table))
