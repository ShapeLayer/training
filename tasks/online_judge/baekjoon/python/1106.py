from sys import stdin
input = stdin.readline

MAX = int(2e10)

def compute(c: int, n: int, costs: list[tuple[int]]):
    dp = [MAX for _i in range(c + 100)]
    dp[0] = 0
    for i in range(1, c + 100):
        for cost in costs:
            pain, gain = cost
            if i - gain >= 0:
                dp[i] = min(dp[i - gain] + pain, dp[i])
    return min(dp[c:])

if __name__ == '__main__':
    c, n = map(int, input().split())
    costs: list[tuple[int]] = [tuple(map(int, input().split())) for _i in range(n)]
    print(compute(c, n, costs))
