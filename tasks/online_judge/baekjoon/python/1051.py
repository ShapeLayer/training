from sys import stdin
input = stdin.readline

def proc(n: int, m: int, rect: list[str]):
    x, y = 0, 0
    corner_len = 1
    while y < n:
        dt = 0
        if x >= m:
            y += 1
            x = 0
            continue
        pn = rect[y][x]
        rx, ry = x, y
        while rx < m and ry < n:
            if pn == rect[y + dt][x] == rect[y][x + dt] == rect[ry][rx]:
                if corner_len < dt + 1:
                    corner_len = dt + 1
            dt += 1
            rx, ry = x + dt, y + dt
        x += 1
    return corner_len ** 2

if __name__ == '__main__':
    n, m = map(int, input().split())
    rect = [input().strip() for _i in range(n)]
    print(proc(n, m, rect))
