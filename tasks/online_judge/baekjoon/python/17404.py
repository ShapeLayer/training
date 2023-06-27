from sys import stdin
input = stdin.readline

MAX = int(1e10)

def compute(n: int, costs: list[tuple[int]]) -> int:
    result = MAX
    for i in range(3): # select start color
        dp: list[list[int]] = [[MAX, MAX, MAX] for _i in range(n)]
        dp[0][i] = costs[0][i]
        for j in range(1, n):
            dp[j][0] = costs[j][0] + min(dp[j - 1][1], dp[j - 1][2])
            dp[j][1] = costs[j][1] + min(dp[j - 1][0], dp[j - 1][2])
            dp[j][2] = costs[j][2] + min(dp[j - 1][0], dp[j - 1][1])
        for j in range(3):
            if i != j: # if equal then color[0] == cost[-1]
                if result > dp[-1][j]:
                    result = dp[-1][j]
    return result

if __name__ == '__main__':
    n = int(input())
    costs: list[tuple[int]] = [tuple(map(int, input().split())) for _i in range(n)]
    print(compute(n, costs))
