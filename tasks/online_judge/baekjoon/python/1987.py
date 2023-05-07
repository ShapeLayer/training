from sys import stdin
input = stdin.readline
A: int = 65
DT = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def compute(r: int, c: int, table: list[str]) -> int:
    passed: list[int] = [0 for _i in range(26)]

    def run(y: int, x: int, cnt: int) -> int:
        if cnt == 26: return cnt

        now = table[y][x]
        oidx = ord(now) - A

        passed[oidx] = True
        cnt += 1
        result = cnt
        for dt in DT:
            dy, dx = dt
            ny, nx = y + dy, x + dx
            if not (0 <= ny < r and 0 <= nx < c): continue
            if passed[ord(table[ny][nx]) - A]: continue
            ran = run(ny, nx, cnt)
            if ran > result:
                result = ran
        passed[oidx] = False
        return result

    return run(0, 0, 0)

if __name__ == '__main__':
    r, c = map(int, input().split())
    table: list[str] = [input().strip() for _i in range(r)]
    print(compute(r, c, table))
