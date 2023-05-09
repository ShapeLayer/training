from sys import stdin
input = stdin.readline
A: int = 65
DT = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def compute(r: int, c: int, table: list[str]) -> int:
    passed: list[int] = [False for _i in range(26)]
    queue = [(0, 0, 0, passed)]
    result = 0

    while queue:
        y, x, cnt, p = queue.pop()
        now = table[y][x]
        o = ord(now) - A

        p[o] = True
        cnt += 1
        if cnt > result:
            result = cnt

        for dt in DT:
            dy, dx = dt
            ny, nx = y + dy, x + dx
            if not (0 <= ny < r and 0 <= nx < c): continue
            if p[ord(table[ny][nx]) - A]: continue
            queue.append((ny, nx, cnt, p.copy()))
    return result

if __name__ == '__main__':
    r, c = map(int, input().split())
    table: list[str] = [input().strip() for _i in range(r)]
    print(compute(r, c, table))
