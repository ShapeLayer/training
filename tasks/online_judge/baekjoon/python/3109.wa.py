from sys import stdin
input = stdin.readline

r, c = map(int, input().split())
_map = [input().strip() for _i in range(r)]
visited = [[False for i in range(c)] for j in range(r)]
dt = [(1, -1), (1, 0), (1, 1)]
count = 0

def visit(x, y):
    global count
    if x == c - 1:
        count += 1
        return True
    for dx, dy in dt:
        nx, ny = x + dx, y + dy
        if ny < 0 or ny >= r:
            continue
        if _map[ny][nx] == 'x':
            continue
        if visited[ny][nx]:
            continue
        visited[ny][nx] = visit(nx, ny)
        if visited[ny][nx]:
            return True
    return False

for i in range(r):
    visited[i][0] = True
    visit(0, i)

print(count)
