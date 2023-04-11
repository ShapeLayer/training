from sys import stdin
input = stdin.readline

r, c = map(int, input().split())
board = []
for _i in range(r):
    board.append(input().strip())

offset = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def dfs(x: int, y: int, count: int, passed: list[bool], max_count: int) -> int:
    for dx, dy in offset:
        nx, ny = x + dx, y + dy
        if nx < 0 or ny < 0 or nx >= c or ny >= r: continue
        now = ord(board[ny][nx]) - 65
        if passed[now]: continue
        count += 1
        passed[now] = True
        est_count = dfs(nx, ny, count, passed, max_count)
        if max_count < count: max_count = count
        if max_count < est_count: max_count = est_count
        count -= 1
        passed[now] = False
    return max_count

passed = [False for _i in range(26)]
passed[ord(board[0][0]) - 65] = True
result = dfs(0, 0, 1, passed, 1)

print(result)
