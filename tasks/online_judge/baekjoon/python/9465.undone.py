from sys import stdin
input = stdin.readline

def compute(n: int, stickers: list[list[int]]):
    dp = [[[max(row[j:k + 1] + [0]) if j > k else max(row[k:j + 1] + [0]) for k in range(n)] for j in range(n)] for row in stickers]
    _max = int(-1e10)
    for i in range(2):
        for j in range(n):
            remain_row = (i + 1) % 2
            now = -1
            if j != 0 and j != n - 1:
                now = stickers[i][j] + max(dp[remain_row][0][j - 1], dp[remain_row][j + 1][n - 1])
            elif j == 0:
                now = stickers[i][j] + dp[remain_row][j + 1][n - 1]
            elif j == n - 1:
                now = stickers[i][j] + dp[remain_row][0][j - 1]
            if now > _max:
                _max = now
    return _max

if __name__ == '__main__':
    for _t in range(int(input())):
        n = int(input())
        stickers: list[list[int]] = [list(map(int, input().split())) for _i in range(2)]
        print(compute(n, stickers))