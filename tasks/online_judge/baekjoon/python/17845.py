from sys import stdin
input = stdin.readline

def compute(n: int, k: int, gets: list[list[int]]) -> int:
    dp = [[0 for _i in range(n + 1)] for _j in range(k + 1)]

    for i in range(1, k + 1):
        for j in range(1, n + 1):
            gain, cost = gets[i - 1]
            if j - cost < 0:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cost] + gain)
    
    return dp[k][n]

if __name__ == '__main__':
    n, k = map(int, input().split())
    gets = [[*map(int, input().split())] for _i in range(k)]
    print(compute(n, k, gets))
