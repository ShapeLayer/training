n, k = map(int, input().split())

dp = [[0 for _i in range(n + 1)] for _j in range(k + 1)]

for i in range(n + 1):
    dp[1][i] = 1

for i in range(1, k + 1):
    for j in range(n + 1):
        for _k in range(j + 1):
            dp[i][j] = (dp[i][j] + dp[i - 1][j - _k]) % 1_000_000_000

print(dp[k][n])
