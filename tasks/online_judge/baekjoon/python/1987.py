from sys import stdin
input = stdin.readline

r, c = map(int, input().split())
board = []
for _i in range(r):
    board.append(input().strip())

offset = [(1, 0), (0, 1), (-1, 0), (0, -1)]

res = 0
def dfs(x: int, y: int, passed: str) -> int:
    global res
    for dx, dy in offset:
        nx, ny = x + dx, y + dy
        if 0 <= nx < c and 0 <= ny < r and board[ny][nx] not in passed: 
            dfs(nx, ny, passed + board[ny][nx])
    if len(passed) > res: res = len(passed)

dfs(0, 0, board[0][0])
print(res)
