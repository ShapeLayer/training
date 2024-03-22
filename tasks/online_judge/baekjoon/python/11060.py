MAX = int(1e10)
n = int(input())
ai = [*map(int, input().split())]
dp = [MAX for i in range(n)]
dp[0] = 0
for i in range(n):
    each = ai[i]
    for j in range(min(i + 1, n - 1), min(i + each + 1, n)):
        dp[j] = min(dp[j], dp[i] + 1)
print(dp[n - 1] if dp[n - 1] != MAX else -1)
