from sys import stdin
input = stdin.readline

def compute(table: list[list[int]], zeors: list[tuple[int]]):
    ables_template = {i: True for i in range(0, 10)}

    def bt(n: int):
        if n == len(zeros):
            for row in table:
                print(*row, sep='')
            exit()

        y, x = zeros[n]
        oy, ox = y // 3, x // 3
        ables = ables_template.copy()

        for i in range(3 * oy, (oy + 1) * 3):
            for j in range(3 * ox, (ox + 1) * 3):
                if ables[table[i][j]]:
                    ables[table[i][j]] = False

        for i in range(9):
            if ables[table[y][i]]:
                ables[table[y][i]] = False
            if ables[table[i][x]]:
                ables[table[i][x]] = False

        for i in ables:
            if not ables[i]:
                continue
            table[y][x] = i
            bt(n + 1)
        table[y][x] = 0
    bt(0)
    return

if __name__ == '__main__':
    table: list[list[int]] = []
    zeros: list[tuple[int]] = []
    for i in range(9):
        row_raw: str = input().strip()
        row: list[int] = []
        for j in range(9):
            tile = int(row_raw[j])
            row.append(tile)
            if tile == 0:
                zeros.append((i, j))
        table.append(row)
    compute(table, zeros)
