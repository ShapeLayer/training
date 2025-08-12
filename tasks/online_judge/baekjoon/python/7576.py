from sys import stdin
from collections import deque
input = stdin.readline

def compute(field: list, N: int, M: int, tomatoes: list) -> int:
    q = deque()
    for tomato in tomatoes:
        q.append(tomato)

    while q:
        y, x = q.popleft()

        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ny, nx = y + dy, x + dx

            if not (0 <= ny < N and 0 <= nx < M):
                continue

            if field[ny][nx] == -1:
                continue

            if field[ny][nx] != 0:
                continue

            field[ny][nx] = field[y][x] + 1
            q.append((ny, nx))

    set_field = set()
    for row in field:
        set_field.update(row)

    if 0 in set_field:
        return -1
    return max(set_field) - 1

if __name__ == "__main__":
    M, N = map(int, input().split())
    field = []
    tomatoes = []
    for i in range(N):
        row = [*map(int, input().split())]
        field.append(row)
        for j in range(M):
            if row[j] == 1:
                tomatoes.append((i, j))
    print(compute(field, N, M, tomatoes))
