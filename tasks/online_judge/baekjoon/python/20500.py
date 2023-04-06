M = 1000000007
n = int(input())
dp = [[-1 for _i in range(1516)] for _j in range(3)]
dp[0][1] = 0
dp[0][2] = 1
dp[1][2] = 1
dp[2][2] = 0

for i in range(3, n + 1):
    dp[0][i] = (dp[2][i - 1] + dp[1][i - 1]) % M
    dp[1][i] = (dp[0][i - 1] + dp[2][i - 1]) % M
    dp[2][i] = (dp[1][i - 1] + dp[0][i - 1]) % M

print(dp[0][n])
