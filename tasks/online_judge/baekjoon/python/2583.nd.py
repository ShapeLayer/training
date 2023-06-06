from sys import stdin
input = stdin.readline

def compute(m: int, n: int, k: int, colored: list[list[int]]) -> list[int]:
    visited: list[list[bool]] = [[False for _i in range(n)] for _j in range(m)]
    for each in colored:
        x1, y1, x2, y2 = each
        for i in range(y1, y2):
            for j in range(x1, x2):
                if not visited[i][j]:
                    visited[i][j] = True

    counts: list[int] = []
    for i in range(m):
        for j in range(n):
            if visited[i][j]:
                continue
            queue: list[tuple[int]] = [(i, j)]
            count = 0
            while queue:
                y, x = queue.pop()
                print(y, x)
                visited[y][x] = True
                count += 1
                for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    ny, nx = y + dy, x + dx
                if 0 <= ny < m and 0 <= nx < n and not visited[ny][nx]:
                    queue.append((ny, nx))
            counts.append(count)
    return sorted(counts)

if __name__ == '__main__':
    m, n, k = map(int, input().split())
    colored: list[tuple[int]] = [tuple(map(int, input().split())) for _i in range(k)]
    counts: list[int] = compute(m, n, k, colored)
    print(len(counts))
    print(*counts)
