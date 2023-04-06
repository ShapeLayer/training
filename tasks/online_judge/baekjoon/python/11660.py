from sys import stdin
input = stdin.readline

if __name__ == '__main__':
    n, m = map(int, input().split())
    table = [[0] * (n+1)] + [[0] + list(map(int, input().split())) for _i in range(n)]
    dp = [[0] * (n+1) for _i in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, n+1):
            dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + table[i][j]

    for _i in range(m):
        x1, y1, x2, y2 = map(int, input().split())
        print(dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1])
