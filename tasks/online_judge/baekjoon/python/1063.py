from sys import stdin
input = stdin.readline

p = lambda pos: (ord(pos[0]) - 65, int(pos[1]) - 1)

king, stone, n = input().split()
king, stone = p(king), p(stone)
n = int(n)

dt = {
    'R': (1, 0),
    'L': (-1, 0),
    'B': (0, -1),
    'T': (0, 1),
    'RT': (1, 1),
    'LT': (-1, 1),
    'RB': (1, -1),
    'LB': (-1, -1)
}

for oper in [input().strip() for _i in range(n)]:
    nk = (king[0] + dt[oper][0], king[1] + dt[oper][1])
    if not (0 <= nk[0] < 8 and 0 <= nk[1] < 8):
        continue
    ns = stone
    if nk == ns:
        ns = (stone[0] + dt[oper][0], stone[1] + dt[oper][1])
        if not (0 <= ns[0] < 8 and 0 <= ns[1] < 8):
            continue
    king, stone = nk, ns

print(f'{chr(king[0] + 65)}{int(king[1]) + 1}')
print(f'{chr(stone[0] + 65)}{int(stone[1]) + 1}')
