n = int(input())
dp = [list(map(int, input().split())) for _i in range(n)]

for i in range(1, n):
    dp[i][0] += min(dp[i-1][1], dp[i-1][2])
    dp[i][1] += min(dp[i-1][0], dp[i-1][2])
    dp[i][2] += min(dp[i-1][0], dp[i-1][1])
print(min(dp[-1]))