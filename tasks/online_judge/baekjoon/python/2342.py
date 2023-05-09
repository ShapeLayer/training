COST_TABLE = [ # [from][to]
    [1, 2, 2, 2, 2],
    [3, 1, 3, 4, 3],
    [3, 3, 1, 3, 4],
    [3, 4, 3, 1, 3],
    [3, 3, 4, 3, 1]
]
M = int(2e10)

def compute(n: int, opers: list[int]) -> int:
    dp = [[[2e10 for _i in range(5)] for _j in range(5)] for _k in range(n + 1)]
    # dp[i][l][r]
    dp[-1][0][0] = 0

    for i in range(n):
        for r in range(5):
            for pl in range(5):
                cost = COST_TABLE[pl][opers[i]]
                dp[i][opers[i]][r] = min(dp[i][opers[i]][r], dp[i - 1][pl][r] + cost)
        for l in range(5):
            for pr in range(5):
                cost = COST_TABLE[pr][opers[i]]
                dp[i][l][opers[i]] = min(dp[i][l][opers[i]], dp[i - 1][l][pr] + cost)
    
    result = M
    for l in range(5):
        for r in range(5):
            result = min(result, dp[n - 1][l][r])
    return result

if __name__ == '__main__':
    opers = list(map(int, input().split()))
    print(compute(len(opers) - 1, opers[:-1]))
