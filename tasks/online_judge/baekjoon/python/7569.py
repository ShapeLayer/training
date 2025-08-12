from sys import stdin
from collections import deque
input = stdin.readline

def compute(field: list, H: int, N: int, M: int, tomatoes: list) -> int:
    q = deque()
    for tomato in tomatoes:
        q.append(tomato)

    while q:
        z, y, x = q.popleft()
        for dz, dy, dx in [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]:
            nz, ny, nx = z + dz, y + dy, x + dx

            if not (0 <= nz < H and 0 <= ny < N and 0 <= nx < M):
                continue

            if field[nz][ny][nx] == -1:
                continue

            if field[nz][ny][nx] != 0:
                continue

            field[nz][ny][nx] = field[z][y][x] + 1
            q.append((nz, ny, nx))

    set_field = set()
    for plane in field:
        for row in plane:
            set_field.update(row)

    if 0 in set_field:
        return -1
    return max(set_field) - 1

if __name__ == "__main__":
    M, N, H = map(int, input().split())
    field = []
    tomatoes = []
    for i in range(H):
        plane = []
        for j in range(N):
            row = [*map(int, input().split())]
            plane.append(row)
            for k in range(M):
                if row[k] == 1:
                    tomatoes.append((i, j, k))
        field.append(plane)
    print(compute(field, H, N, M, tomatoes))
