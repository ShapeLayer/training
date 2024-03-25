from sys import stdin
input = stdin.readline

L, R = -1, 1
MOVE, TURN = 0, 1
N, E, S, W = 0, 1, 2, 3
DN, DE, DS, DW = (0, 1), (1, 0), (0, -1), (-1, 0)
DT = [DN, DE, DS, DW]

class OperationInvalidError(Exception):
    pass

def parse(oper, param):
    return ([MOVE, TURN][oper != 'MOVE'], [L, R][int(param)] if oper == 'TURN' else int(param))

def compute(m: int, n: int, opers: list[tuple[int]]):
    y, x, d = 0, 0, E
    for oper, param in opers:
        if oper == MOVE:
            y, x = y + DT[d][1] * param, x + DT[d][0] * param
            if not (0 <= y <= m and 0 <= x <= m):
                raise OperationInvalidError
        elif oper == TURN:
            d = (d + param) % 4
    return y, x

if __name__ == '__main__':
    m, n = map(int, input().split())
    opers = [parse(*input().split()) for _i in range(n)]
    y, x = -1, -1
    try:
        y, x = compute(m, n, opers)
        print(x, y)
    except OperationInvalidError:
        print(-1)
