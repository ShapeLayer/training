from sys import stdin
input = stdin.readline

OFFSETS = [(1, 0), (0, 1)]

def compute(n: int, table: list[list[int]]) -> int:
    queue: list[tuple[int]] = [(0, 0)]
    counts: int = 0
    while queue:
        y, x = queue.pop()
        now = table[y][x]
        for oy, ox in OFFSETS:
            ny, nx = y + now * oy, x + now * ox
            if 0 <= ny < n and 0 <= nx < n:
                if ny == nx == n - 1:
                    counts += 1
                    continue
                if table[ny][nx] == 0:
                    continue
                queue.append((ny, nx))
    return counts

if __name__ == '__main__':
    n: int = int(input())
    table: list[list[int]] = [list(map(int, input().split())) for _i in range(n)]
    print(compute(n, table))
