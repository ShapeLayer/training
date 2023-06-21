MOD = 1_000_000_007

'''
정보과학관 0
전산관 1
미래관 2
신양관 3
한경직기념관 4
진리관 5
학생회관 6
형남공학관 7
'''

conn: list[list[int]] = [[0 for _i in range(8)] for _j in range(8)]

def init_conn():
    conn[0][1] = 1
    conn[0][2] = 1
    conn[1][0] = 1
    conn[1][2] = 1
    conn[1][3] = 1
    conn[2][0] = 1
    conn[2][1] = 1
    conn[2][3] = 1
    conn[2][4] = 1
    conn[3][1] = 1
    conn[3][2] = 1
    conn[3][4] = 1
    conn[3][5] = 1
    conn[4][2] = 1
    conn[4][3] = 1
    conn[4][5] = 1
    conn[4][7] = 1
    conn[5][3] = 1
    conn[5][4] = 1
    conn[5][6] = 1
    conn[6][5] = 1
    conn[6][7] = 1
    conn[7][4] = 1
    conn[7][6] = 1

dp: dict = {} # key: dist
dp[1] = conn


def compute(dist: int) -> int:
    def each(dist: int, from_: int, to: int) -> int:
        if dist <= 1:
            return dp[dist][from_][to]

        dp.setdefault(dist, [[0 for _i in range(8)] for _j in range(8)])
        if dp[dist][from_][to]:
            return dp[dist][from_][to]
        
        mid = dist // 2
        other = mid if dist % 2 == 0 else mid + 1

        for i in range(8):
            dp[dist][from_][to] = (dp[dist][from_][to] + each(mid, from_, i) * each(other, i, to)) % MOD

        return dp[dist][from_][to]
    
    return each(dist, 0, 0)

if __name__ == '__main__':
    init_conn()
    n = int(input())
    print(compute(n))
