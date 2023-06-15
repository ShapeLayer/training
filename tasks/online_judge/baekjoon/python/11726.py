def compute(n: int) -> int:
    dp = [0 for _i in range(n + 1)]
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = (dp[i - 2] + dp[i - 1]) % 10007
    return dp[n]

if __name__ == '__main__':
    n = int(input())
    print(compute(n))
