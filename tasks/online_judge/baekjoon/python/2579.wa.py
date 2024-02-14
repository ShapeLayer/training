from sys import stdin
input = stdin.readline

n = int(input())
stairs = [0] + [int(input()) for _i in range(n)]
dp = [0 for i in range(n + 1)]

dp[1] = stairs[1]
for i in range(n + 1):
    if i - 2 >= 0:
        dp[i] = max(dp[i], dp[i - 2] + stairs[i])
    print(i, dp[i])
    if i - 3 >= 0:
        dp[i] = max(dp[i], dp[i - 3] + stairs[i - 2] + stairs[i])
    print(i, dp[i])
    if i - 4 >= 0:
        dp[i] = max(dp[i], dp[i - 4] + stairs[i - 3] + stairs[i - 2] + stairs[i])
    print(i, dp[i])

dp[n] = max(dp[n], dp[n - 1] + stairs[n])
print(dp[n])
