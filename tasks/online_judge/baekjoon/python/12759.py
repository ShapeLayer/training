from sys import stdin
input = stdin.readline

def compute(opers: list[tuple[int]]) -> int:
    table = [[-1 for _i in range(4)] for _j in range(4)]
    player = 0
    
    def evaluate() -> bool:
        if table[1][1] == table[2][2] == table[3][3] == player:
            return True
        if table[3][1] == table[2][2] == table[1][3] == player:
            return True
        for i in range(1, 4):
            if table[i][1] == table[i][2] == table[i][3] == player:
                return True
            if table[1][i] == table[2][i] == table[3][i] == player:
                return True
        return False
    
    for oper in opers:
        y, x = oper
        table[y][x] = player
        if evaluate():
            return player
        player = (player + 1) % 2
    return -1

if __name__ == '__main__':
    starts: int = int(input())
    opers: list[tuple[int]] = [tuple(map(int, input().split())) for _i in range(9)]
    result = compute(opers)
    if result < 0:
        print(0)
    elif result == 0:
        print(starts)
    else:
        print(starts % 2 + 1)
