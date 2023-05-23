from sys import stdin
input = stdin.readline

NR, ES, SU, WS = 0, 1, 2, 3

def compute(n: int, m: int, r: int, c: int, d: int, table: list[list[int]]) -> int:
    cleanings: int = 0

    def calc_dt(d: int) -> tuple[int]:
        if d == NR:
            return -1, 0
        if d == ES:
            return 0, 1
        if d == SU:
            return 1, 0
        return 0, -1
    
    def is_block(y: int, x: int) -> bool:
        return (0 <= y < n and 0 <= x < m) and table[y][x] != 1
    
    def near_is_dirty(y: int, x: int) -> bool:
        for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ny, nx = y + dy, x + dx
            if is_block(ny, nx):
                if table[ny][nx] == 0:
                    return True
        return False
    
    def get_pos_using_dt(y: int, x: int, d: int) -> tuple[int]:
        dy, dx = calc_dt(d)
        return y + dy, x + dx
    
    def cleaning(y: int, x: int, cleanings: int) -> int:
        table[y][x] = 2
        cleanings += 1
        return cleanings

    y, x = r, c
    if table[y][x] == 0:
        cleanings = cleaning(y, x, cleanings)

    while True:
        if near_is_dirty(y, x):
            for _i in range(4):
                d = (d + 3) % 4
                ny, nx = get_pos_using_dt(y, x, d)
                if is_block(ny, nx) and table[ny][nx] == 0:
                    y, x = ny, nx
                    cleanings = cleaning(y, x, cleanings)
                    break
        else:
            dy, dx = calc_dt(d)
            dy, dx = -dy, -dx
            ny, nx = y + dy, x + dx
            if is_block(ny, nx) and table[ny][nx] != 1:
                y, x = ny, nx
                continue
            else:
                break
    return cleanings

if __name__ == '__main__':
    n, m = map(int, input().split())
    r, c, d = map(int, input().split())
    table: list[list[int]] = [list(map(int, input().split())) for _i in range(n)]
    print(compute(n, m, r, c, d, table))
