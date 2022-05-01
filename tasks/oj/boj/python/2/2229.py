n = int(input())
gets = list(map(int, input().split()))
dp = [0 for _ in range(n)]
for i in range(1, n):
    for j in range(1, i+2):
        now = gets[i-j+1:i+1]
        if j == i + 1:
            j = i
        dp[i] = max(dp[i], dp[i-j] + max(now) - min(now))

print(dp[n-1])