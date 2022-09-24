UNDEF = -1
MINE = -2
VOID = -3

n = int(input())
tiles = [[0] * n] * n
for i in range(n):
    tiles[i] = [UNDEF if each_dot == '#' else int(each_dot) for each_dot in list(input())]

total_mines = 0
for i in range(n):
    for j in range(n):
        if 1 <= i <= n-2 and 1 <= j <= n-2: continue
        now = tiles[i][j]
        if now < 0: continue
        mines_checked = 0
        voids = 0
        for dt in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            nt = (dt[0] + i, dt[1] + j)
            if not (0 <= nt[0] < n and 0 <= nt[1] < n): continue
            if tiles[nt[0]][nt[1]] == MINE: mines_checked += 1
            if tiles[nt[0]][nt[1]] == VOID or tiles[nt[0]][nt[1]] == MINE: voids += 1
        for dt in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            nt = (dt[0] + i, dt[1] + j)
            if not (0 <= nt[0] < n and 0 <= nt[1] < n): continue
            if tiles[nt[0]][nt[1]] == UNDEF:
                if mines_checked < now:
                    mines_checked += 1
                    tiles[nt[0]][nt[1]] = MINE
                    total_mines += 1
                else:
                    tiles[nt[0]][nt[1]] = VOID

print(total_mines + (n-4 if n-4 > 0 else 0) ** 2)